de2en = {
    "eins": "one",
    "zwei": "two",
    "drei": "three",
    "vier": "four",
    "fünf": "five",
    }
def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())

