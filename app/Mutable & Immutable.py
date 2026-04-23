# 8 zmiennych różnych typów
a = 100             # int (immutable)
b = "Python"        # str (immutable)
c = [1, 2, 3]       # list (mutable)
d = (4, 5)          # tuple (immutable)
e = {"key": "val"}  # dict (mutable)
f = 3.14            # float (immutable)
g = {1, 2, 3}       # set (mutable)
h = True            # bool (immutable)

# Podział do słownika
sorted_variables = {
    "mutable": [c, e, g],
    "immutable": [a, b, d, f, h]
}

# Wyświetlenie wyniku
print(sorted_variables)
