def count_occurrences(phrase, letter):
    count = 0

    for character in phrase:
        if character.lower() == letter.lower():
            count += 1

    return count