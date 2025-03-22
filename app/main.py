def count_occurrences(phrase: str, letter: str) -> int:
    """
    Count occurrences of a letter in a phrase (case insensitive).

    :param phrase: The phrase to search within.
    :param letter: The letter to count occurrences of.
    :return: The number of occurrences of the letter in the phrase.
    """

    #return phrase.lower().count(letter.lower())
    #Not sure if you are better off doing this as one line or if you should make variables first.
    #I ended up splitting into variables just in case, but the above should work as well.

    phrase_lower = phrase.lower()
    final_phrase = phrase_lower.count(letter.lower())
    return final_phrase

