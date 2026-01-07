import pytest
import ast
import inspect

from app import main
from app.main import (
    format_linter_error,
    format_single_linter_file,
    format_linter_report,
)


@pytest.mark.parametrize(
    "error_linter,error_mate",
    [
        (
            {
                "code": "E501",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 80,
                "text": "line too long (99 > 79 characters)",
                "physical_line": '    return f"I like to filter, rounding, doubling, '
                "store and decorate numbers: {', '.join(items)}!\"",
            },
            {
                "line": 18,
                "column": 80,
                "message": "line too long (99 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
        ),
        (
            {
                "code": "E702",
                "filename": "./source_code_1.py",
                "line_number": 3,
                "column_number": 74,
                "text": "multiple statements on one line (semicolon)",
                "physical_line": '        new_items = [f"{key} -> {value}" for key, '
                "value in items.items()]; return func(new_items)\n",
            },
            {
                "line": 3,
                "column": 74,
                "message": "multiple statements on one line (semicolon)",
                "name": "E702",
                "source": "flake8",
            },
        ),
        (
            {
                "code": "E302",
                "filename": "./source_code_1.py",
                "line_number": 15,
                "column_number": 1,
                "text": "expected 2 blank lines, found 1",
                "physical_line": "def number_filter(func):\n",
            },
            {
                "line": 15,
                "column": 1,
                "message": "expected 2 blank lines, found 1",
                "name": "E302",
                "source": "flake8",
            },
        ),
    ],
)
def test_format_linter_error(error_linter, error_mate):
    assert format_linter_error(error_linter) == error_mate, (
        f"Function 'format_linter_error' should return {error_mate}, "
        f"when 'error' equals to {error_linter}"
    )


@pytest.mark.parametrize(
    "func",
    [
        format_linter_error,
        format_single_linter_file,
        format_linter_report,
    ],
)
def test_format_functions_one_line(func):
    code = inspect.getsource(func)
    assert (
        isinstance(ast.parse(code).body[0].body[0], ast.Return) is True
    ), f"Function '{func.__name__}' should contain only return statement"


@pytest.mark.parametrize(
    "file_path,errors,result",
    [
        (
            "./source_code_2.py",
            [
                {
                    "code": "E501",
                    "filename": "./source_code_2.py",
                    "line_number": 18,
                    "column_number": 80,
                    "text": "line too long (99 > 79 characters)",
                    "physical_line": '    return f"I like to filter, rounding, doubling, '
                    "store and decorate numbers: {', '.join(items)}!\"",
                },
                {
                    "code": "W292",
                    "filename": "./source_code_2.py",
                    "line_number": 18,
                    "column_number": 100,
                    "text": "no newline at end of file",
                    "physical_line": '    return f"I like to filter, rounding, doubling, '
                    "store and decorate numbers: {', '.join(items)}!\"",
                },
            ],
            {
                "errors": [
                    {
                        "line": 18,
                        "column": 80,
                        "message": "line too long (99 > 79 characters)",
                        "name": "E501",
                        "source": "flake8",
                    },
                    {
                        "line": 18,
                        "column": 100,
                        "message": "no newline at end of file",
                        "name": "W292",
                        "source": "flake8",
                    },
                ],
                "path": "./source_code_2.py",
                "status": "failed",
            },
        )
    ],
)
def test_format_single_linter_file(file_path, errors, result):
    assert format_single_linter_file(file_path, errors) == result, (
        f"Function 'format_single_linter_file' should return {result}, "
        f"when 'file_path' equals to {file_path}, "
        f"and 'errors' equals to {errors}"
    )


@pytest.mark.parametrize(
    "errors_linter,errors_mate",
    [
        (
            {
                "./test_source_code_2.py": [],
                "./source_code_2.py": [
                    {
                        "code": "E501",
                        "filename": "./source_code_2.py",
                        "line_number": 18,
                        "column_number": 80,
                        "text": "line too long (99 > 79 characters)",
                        "physical_line": '    return f"I like to filter, rounding, doubling, '
                        "store and decorate numbers: {', '.join(items)}!\"",
                    },
                    {
                        "code": "W292",
                        "filename": "./source_code_2.py",
                        "line_number": 18,
                        "column_number": 100,
                        "text": "no newline at end of file",
                        "physical_line": '    return f"I like to filter, rounding, doubling, '
                        "store and decorate numbers: {', '.join(items)}!\"",
                    },
                ],
                "./source_code_1.py": [
                    {
                        "code": "E702",
                        "filename": "./source_code_1.py",
                        "line_number": 3,
                        "column_number": 74,
                        "text": "multiple statements on one line (semicolon)",
                        "physical_line": '        new_items = [f"{key} -> {value}" for key, '
                        "value in items.items()]; return func(new_items)\n",
                    },
                    {
                        "code": "E501",
                        "filename": "./source_code_1.py",
                        "line_number": 3,
                        "column_number": 80,
                        "text": "line too long (97 > 79 characters)",
                        "physical_line": '        new_items = [f"{key} -> {value}" for key, '
                        "value in items.items()]; return func(new_items)\n",
                    },
                    {
                        "code": "E302",
                        "filename": "./source_code_1.py",
                        "line_number": 15,
                        "column_number": 1,
                        "text": "expected 2 blank lines, found 1",
                        "physical_line": "def number_filter(func):\n",
                    },
                    {
                        "code": "E303",
                        "filename": "./source_code_1.py",
                        "line_number": 27,
                        "column_number": 1,
                        "text": "too many blank lines (6)",
                        "physical_line": "@number_filter\n",
                    },
                    {
                        "code": "E501",
                        "filename": "./source_code_1.py",
                        "line_number": 31,
                        "column_number": 80,
                        "text": "line too long (99 > 79 characters)",
                        "physical_line": '    return f"I like to filter, rounding, doubling, '
                        "store and decorate numbers: {', '.join(items)}!\"\n",
                    },
                ],
                "./test_source_code_1.py": [
                    {
                        "code": "E302",
                        "filename": "./test_source_code_1.py",
                        "line_number": 4,
                        "column_number": 1,
                        "text": "expected 2 blank lines, found 1",
                        "physical_line": "@pytest.mark.parametrize(\n",
                    },
                    {
                        "code": "E501",
                        "filename": "./test_source_code_1.py",
                        "line_number": 32,
                        "column_number": 80,
                        "text": "line too long (84 > 79 characters)",
                        "physical_line": '            "decorate numbers: 1 -> 2, 2 -> 4, 6 -> 12, -111 -> -222, -50 -> '
                        '-100!",\n',
                    },
                    {
                        "code": "W292",
                        "filename": "./test_source_code_1.py",
                        "line_number": 112,
                        "column_number": 6,
                        "text": "no newline at end of file",
                        "physical_line": "    )",
                    },
                ],
            },
            [
                {"errors": [], "path": "./test_source_code_2.py", "status": "passed"},
                {
                    "errors": [
                        {
                            "line": 18,
                            "column": 80,
                            "message": "line too long (99 > 79 characters)",
                            "name": "E501",
                            "source": "flake8",
                        },
                        {
                            "line": 18,
                            "column": 100,
                            "message": "no newline at end of file",
                            "name": "W292",
                            "source": "flake8",
                        },
                    ],
                    "path": "./source_code_2.py",
                    "status": "failed",
                },
                {
                    "errors": [
                        {
                            "line": 3,
                            "column": 74,
                            "message": "multiple statements on one line (semicolon)",
                            "name": "E702",
                            "source": "flake8",
                        },
                        {
                            "line": 3,
                            "column": 80,
                            "message": "line too long (97 > 79 characters)",
                            "name": "E501",
                            "source": "flake8",
                        },
                        {
                            "line": 15,
                            "column": 1,
                            "message": "expected 2 blank lines, found 1",
                            "name": "E302",
                            "source": "flake8",
                        },
                        {
                            "line": 27,
                            "column": 1,
                            "message": "too many blank lines (6)",
                            "name": "E303",
                            "source": "flake8",
                        },
                        {
                            "line": 31,
                            "column": 80,
                            "message": "line too long (99 > 79 characters)",
                            "name": "E501",
                            "source": "flake8",
                        },
                    ],
                    "path": "./source_code_1.py",
                    "status": "failed",
                },
                {
                    "errors": [
                        {
                            "line": 4,
                            "column": 1,
                            "message": "expected 2 blank lines, found 1",
                            "name": "E302",
                            "source": "flake8",
                        },
                        {
                            "line": 32,
                            "column": 80,
                            "message": "line too long (84 > 79 characters)",
                            "name": "E501",
                            "source": "flake8",
                        },
                        {
                            "line": 112,
                            "column": 6,
                            "message": "no newline at end of file",
                            "name": "W292",
                            "source": "flake8",
                        },
                    ],
                    "path": "./test_source_code_1.py",
                    "status": "failed",
                },
            ],
        )
    ],
)
def test_format_linter_report(errors_linter, errors_mate):
    assert format_linter_report(errors_linter) == errors_mate, (
        f"Function 'format_linter_report' should return {errors_mate} "
        f"when 'errors' equals to {errors_linter}"
    )


def test_comment_deleted():
    lines = inspect.getsource(main)
    assert "# write your code here" not in lines, (
        "Remove the unnecessary" " comment '# write your code here'"
    )


def test_double_quotes_instead_of_single():
    lines = inspect.getsource(main)
    assert "'" not in lines, (
        'You have to use a double quotes "" instead' " of single ''"
    )
