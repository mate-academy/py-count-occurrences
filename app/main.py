def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).
    :param phrase: string to search in
    :param letter: single character to count occurrences of
    :return: number of times `letter` appears in `phrase` (case insensitive)
    """
    return phrase.lower().count(letter.lower())


print(count_occurrences("abca", "b"))
