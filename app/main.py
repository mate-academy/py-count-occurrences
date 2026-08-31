def count_occurrences(phrase: str, letter: str) -> int:
    result_count = 0
    for word in phrase:
        word = word.lower()
        if letter.lower() in word:
            result_count += 1
    return result_count
