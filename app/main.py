def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count the number of occurrences of `letter` in `phrase`.
    The function is case insensitive.
    args:
       phrase: str - to search
       letter: str - to count
    returns: int - number of times `letter` occurs in `phrase`
    examples:           
         count_occurrences("Hello World", "o") -> 2
         count_occurrences("Hello World", "O") -> 2
         count_occurrences("Hello World", "l") -> 3
         count_occurrences("Hello World", "L") -> 3
         count_occurrences("Hello World", "x") -> 0
    """
    return phrase.lower().count(letter.lower())
