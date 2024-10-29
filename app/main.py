def count_occurrences(phrase: str, letter: str) -> int:
    occurrences_count = 0
    for letter_phrase in phrase.lower():
        if letter_phrase == letter.lower():
            occurrences_count += 1
    return occurrences_count


print(count_occurrences("letter", "t"))
