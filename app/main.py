
def count_occurrences(phrase: str, letter: str) -> int:
    """Count occurrences of letter in phrase and return number of occurrences"""
    return phrase.lower().count(letter.lower())
