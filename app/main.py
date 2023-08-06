variable_one = 123
empty_list = []
greeting = "Hi!"
number_list = [1, 2]

def count_occurrences(phrase: str, letter: str) -> int:
    count = 0

    for char in phrase:
        if char.lower() == letter.lower():
            count += 1

    return count
