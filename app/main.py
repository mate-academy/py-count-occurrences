def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    occurrences = 0

    for char in phrase:
        if char.lower() == letter.lower():
            occurrences += 1

    return occurrences
