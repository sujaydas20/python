sum=lambda x,y:x*y
x=int(input("enter your number"))
y=int(input("enter your number"))

print (sum(x,y))






def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))





sum=lambda a:((a+a)*a)+a


print(sum(9))


