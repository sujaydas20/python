""" means that a prvious two number is equel to the next upcoming number
ex
0,1,1,2,3,5,8,13"""

def valu(a,b,c):
    if a+b<c:
        return b+c
    a=0
    b=1
    c=a+b



def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter your range : "))
fibonacci(n)




def fib(n):
    if (n==0 or n==1):
        return n
    return fib(n-2)+(n-1)
print(fib(9))