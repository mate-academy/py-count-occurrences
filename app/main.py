def count_occurrences(phrase, letter):
    counter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
    return counter
