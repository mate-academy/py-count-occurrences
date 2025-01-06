def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for part in phrase:
        if part.lower() == letter.lower():
            count += 1
    return countflake8