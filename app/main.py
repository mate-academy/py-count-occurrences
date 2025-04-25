lucky_number = 7
pi = 3.14
one_is_a_prime_number = False
name = "Yuriy"
my_favourite_films = ["Inception", "Interstellar", "Matrix"]
profile_info = {"name": "Yuriy", "age": 25}
marks = [100, 90, 85, 95]
collection_of_coins = {1, 5, 10, 25}
sorted_variables = [lucky_number,pi,one_is_a_prime_number,name,my_favourite_films,
    profile_info,marks,collection_of_coins,]

def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())



git add app/main.py app/__init__.py
git commit -m "Виправив імпорт count_occurrences"
git push origin new-branch
