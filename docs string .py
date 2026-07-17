def sum(a,b):
    """this will add two number"""
    c=a+b
    return c
print(sum(4,5))
print(sum.__doc__)



# check the maxmum vlaue useing function and docs string



def maximum(a, b):
    """This function checks which number is greater."""

    if a >= b:
        return "a is the greater number"
    else:
        return "b is the greater number"


a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

print(maximum(a, b))
print(maximum.__doc__)

   