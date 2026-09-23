a = [(1, 5), (2, 1), (3, 3)]

b = sorted(a, key=lambda x: x[1])

print(b)



a = 3
b = 4
c = 5

a, b, c = c, a, b

print(a + b * c)