# def sum(a,b):
#     return a+b
# print(sum(555,22))





def sum(*args):
    total=0
    for item in args:
        total+=item
    return total


print(sum(444,888,999,666))