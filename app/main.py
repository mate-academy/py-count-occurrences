"""
def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())
"""

def count_occurrences(phrase: str, letter: str) -> int:
    counter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
    return counter
