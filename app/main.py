def count_occurrences(phrase: str, letter: str) -> int:
    count_letter = phrase.lower().count(letter.lower())

    """
    or this ???
    def count_occurrences(phrase: str, letter: str) -> int:
        phrase_lower = phrase.lower()
        letter_lower = letter.lower()

        count_letter = phrase_lower.count(letter_lower)

    return count_letter
    """
    return count_letter
