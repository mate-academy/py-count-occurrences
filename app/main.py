def count_occurrences(phrase: str, letter: str) -> int:
  lowerCase_phrase = phrase.lower()
  lowerCase_letter = letter.lower()
  count = 0
  for char in lowerCase_phrase:
      if char == lowerCase_letter:
            count += 1
  return count 