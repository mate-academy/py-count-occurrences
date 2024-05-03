"""task count_occurrences"""
def count_occurrences(phrase: str, letter: str) -> int:
    """
    func count latters in phrase
    """
    return phrase.lower().count(letter.lower())
