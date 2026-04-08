def create_dictionary(*args) -> dict:
    result = {}

    key_types = (int, float, str, bool, type(None), tuple)

    for index, arg in enumerate(args):
        if isinstance(arg, key_types) or callable(arg):
            result[arg] = index
        else:
            print(f"Cannot add {arg} to the dict!")

    return result
