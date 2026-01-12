def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    counter = 0
    for char in phrase:
        if char.lower() == letter.lower():
            counter += 1
    return counter
lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}


number = 123
empty_list = []
greeting = "Hi!"
numbers = [1, 2]

sorted_variables = {
    "mutable": [empty_list, numbers],
    "immutable": [number, greeting]
}
