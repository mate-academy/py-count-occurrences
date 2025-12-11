def create_dictionary(*args):
    dic = {}
    
    allowed_types = (int, float, str, bool, type(None), list, tuple, set, dict)
    
    for index, arg in enumerate(args):

        if isinstance(arg, allowed_types) or callable(arg):

            if isinstance(arg, (int, float, str, bool, type(None), tuple)) or callable(arg):
                dic[arg] = index
            else:
                print(f"Cannot add {arg} to the dict!")
        
        else:
            print(f"Cannot add {arg} to the dict!")
    
    return dic
