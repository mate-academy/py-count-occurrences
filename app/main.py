def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    occurrences = 0
    for l in phrase:
        if l == letter:
            occurrences += 1

    return occurrences
