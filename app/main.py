from functools import wraps
from typing import Any, Callable, Dict, Tuple

# Cache storage for each decorated function
_cache_store: Dict[Callable, Dict[Tuple[Any, ...], Any]] = {}


def cache(func: Callable) -> Callable:
    _cache_store[func] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Create a hashable key using args and kwargs
        key = args + tuple(sorted(kwargs.items()))

        if key in _cache_store[func]:
            print("Getting from cache")
            return _cache_store[func][key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        _cache_store[func][key] = result
        return result

    return wrapper
