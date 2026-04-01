def count_occurrences(phrase: str, letter: str) -> int:
    char_count: int = 0
    for char in phrase:
        if char.lower() == letter.lower():
            char_count += 1
    return char_count
    pass
