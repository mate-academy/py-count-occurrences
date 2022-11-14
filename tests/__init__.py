import functools


def cache(func):
    func_result = {}

    @functools.wraps(func)
    def inner(*args):
        if f"{args}" in func_result:
            print("Getting from cache")
        else:
            func_result[f"{args}"] = func(*args)
            print("Calculating new result")
        return func_result[f"{args}"]
    return inner
