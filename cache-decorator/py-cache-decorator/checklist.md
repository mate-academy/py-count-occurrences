# Сheck Your Code Against the Following Points

## Code Efficiency

Don't call the same function several times. Store the result and reuse it.

Good example:

```python
animals = "cat, dog, rabbit"
animals_title = animals.title()
print(animals_title)

for letter in set(animals_title):
    if animals_title.count(letter) > 1:
        print("wow")
```

Bad example:

```python
animals = "cat, dog, rabbit"
print(animals.title())

for letter in set(animals.title()):
    if animals.title().count(letter) > 1:
        print("wow")
```

## Don`t Repeat Yourself 

Write your code, so you don't have duplicated lines or whole blocks of code.

Good example:

```python
if "cat" in animal_list:
    print("found")
else:
    print("not found")

print("the end")
```

Bad example:

```python
if "cat" in animal_list:
    print("found")
    print("the end")
else:
    print("not found")
    print("the end")
```

## Code Style

1. Use descriptive and correct variable names.

Good example:

```python
list_of_numbers = [1, 2, 3, 4]
result = 0
for number in list_of_numbers:
    result += number
```

Bad example:

```python
ls = [1, 2, 3, 4]
rs = 0
for a in ls:
    rs += a
```

2. Use one style of quotes in your code. Double quotes are preferable.

## Clean Code

1. You don't need the `nonlocal` statement when you change a mutable object in inner function.
2. Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
