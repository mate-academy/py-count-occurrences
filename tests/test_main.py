def test_removed_comment():
    lines = inspect.getsource(main)
    assert "# write your code here" not in lines, (
        "You have to remove the unnecessary comment '# write your code here'"
    )
