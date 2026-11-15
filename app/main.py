

def count_occurrences(phrase: str, letter: str) -> int:
    final_phrase = phrase.lower()
    count = final_phrase.count(letter.lower())
    return count
