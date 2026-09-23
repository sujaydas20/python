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




a = [10, 20, 30, 40]

x = a.pop(1)
y = a.pop()

print(x + y)
print(a)




x = 7

y = 10 if x > 8 else 20 if x > 5 else 30

print(y)



a = [[1, 2, 3],
     [4, 5, 6]]

b = [[row[i] for row in a] for i in range(3)]

print(b)



a = [5, 10, 15]

s = 0

for i, x in enumerate(a, start=1):
    s += i * x

print(s)



a = [1, 2, 3, 4]
b = [10, 20]

s = 0

for x, y in zip(a, b):
    s += x + y

print(s)


a = [1, 2, 2, 3, 3, 3, 4]

b = set(a)

print(sum(b))



d = {}

for i in range(4):
    d[i % 2] = i

print(d)



s = "GATE2027"

if s.startswith("GAT"):
    print(s[4:])
else:
    print("No")