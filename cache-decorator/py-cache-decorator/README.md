# Cache decorator
- Read the [guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)  before start

You have a big array with data. You have to run a long runtime function
with this data. Data can be repeated.
To not re-run function with repeatable data, it will be good to store
results of completed runs.


Write decorator `cache` that stores results of completed runs with
different arguments, number of arguments can be also different.
If decorated function runs with repeating arguments it should return stored
result instead of calling function again. Decorator `cache` creating for 
decorating only functions that take **immutable** arguments.

Also note, that decorator `cache` should work correctly with few decorated
functions simultaneously and correctly return for every function separately.

Also `cache` should print `Getting from cache` when returns stored value and 
`Calculating new result` when run function with new arguments.

Example:
```python
@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)

# Calculating new result 
# Calculating new result 
# Calculating new result 
# Getting from cache 
# Calculating new result 
# Getting from cache
```

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
