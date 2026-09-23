a = [(1, 5), (2, 1), (3, 3)]

b = sorted(a, key=lambda x: x[1])

print(b)



a = 3
b = 4
c = 5

a, b, c = c, a, b

print(a + b * c)




a = [2, 3, 2, 4, 2, 5, 3]

x = a.count(2)
y = a.count(3)

print(x * y)




a = [10, 20, 30, 20, 40]

x = a.index(20)
y = a.index(40)

print(x + y)