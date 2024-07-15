def count_occurrences(phrase: str, letter: str) -> int:
    return sum(1 for character in phrase
               if character.lower() == letter.lower())
