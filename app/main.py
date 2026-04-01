phrase = "Hello World"
letter = "l"

# приводимо до одного регістру
phrase_lower = phrase.lower()
letter_lower = letter.lower()

# підрахунок входжень
result = phrase_lower.count(letter_lower)
print(result)  # виведе кількість літер "l" незалежно від регістру
