from typing import Callable


def arrow(func: Callable) -> Callable:
    def wrapper(dict_users: dict) -> list:
        arrowed_values = [f"{key} -> {value}" for key, value in dict_users.items()]
        return func(arrowed_values)
    return wrapper


def number_filter(func: Callable) -> Callable:
    def wrapper(items: list) -> list:
        new_items = [item for item in items if isinstance(item, (int, float))]
        return func(new_items)
    return wrapper


def round_dict(func: Callable) -> Callable:
    def wrapper(new_items: list) -> dict:
        dict_users = {round(item): round(item) * 2 for item in new_items}
        return func(dict_users)
    return wrapper


@number_filter
@round_dict
@arrow
def like_numbers(items: list) -> str:
    print(f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!")


#like_numbers(["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}])

import functools

def decorator(func):
    def inner():
        print("start")
        func()
        print("end")
    return inner

@decorator
def greet_friend(friend):
    print(f"Hi, dear {friend}!")

#greet_friend("Misha")

def repeat_twice(func):
    def inner(*args, **kwargs):
        print("executing!")
        func(*args, **kwargs)
        print(*args)
        print("executing!")
        func(*args, **kwargs)
        print(*args)
        return args
    return inner

@repeat_twice
def double_num(num: int):
    print(num)
    return num * 2

print(double_num(4))
