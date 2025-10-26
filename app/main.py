def count_occurrences(phrase: str, letter: str) -> int:

    fix_phrase = phrase.lower()
    fix_letter = letter.lower()
    return fix_phrase.count(fix_letter)
