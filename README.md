# Count Occurrences

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

## Task Description

You are required to implement the `count_occurrences` function that takes two parameters:

1. **phrase**: A string in which to count occurrences of a letter.
2. **letter**: The letter whose occurrences need to be counted in the given phrase.

The function should return the number of times the letter appears in the phrase, while being **case insensitive**.

### Examples:

- `count_occurrences("letter", "t")` should return `2`
- `count_occurrences("abc", "a")` should return `1`
- `count_occurrences("abc", "d")` should return `0`
- `count_occurrences("ABC", "a")` should return `1`

### Function Signature:

```python
def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """
```

## Guidelines

- The function must be **case insensitive**. This means that both the phrase and the letter should be treated as if they are in the same case (upper or lower).
  
- It is **recommended** to avoid using loops to solve this task. Instead, consider utilizing Python's built-in string functions to simplify the solution.

