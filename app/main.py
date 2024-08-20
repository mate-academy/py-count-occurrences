a = 123
b = []
c = "Hi!"
d = [1, 2]
e = (1, 2)
f = True
g = {"key": "value"}
h = 3.14

sorted_variables = {
    "mutable": [b, d, g],
    "immutable": [a, c, e, f, h]
}

print(sorted_variables)
