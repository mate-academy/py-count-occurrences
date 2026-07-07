def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    phrase = phrase.lower()
    letter = letter.lower()
    for symbole in phrase:
        if symbole == letter:
            count += 1
    return count    

test_count_occurrences = count_occurrences("Abracadabra", "A")

print(test_count_occurrences)

test_count_occurrences = count_occurrences("Samsung is gnusmas", "s")

print(test_count_occurrences)
    
