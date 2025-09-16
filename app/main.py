def count_occurences(phrase: str, letter: str) -> int:
    phrase = phrase.lower()
    letter = letter.lower()
    _dict = {letter: 0}
    for let in phrase:
        if let in _dict:
            _dict[letter] += 1
    return _dict[letter]
