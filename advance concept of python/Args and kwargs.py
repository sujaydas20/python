# def sum(a,b):
#     return a+b
# print(sum(555,22))



# arge

def sum(*args):
    total=0
    for item in args:
        total+=item
    return total


print(sum(444,888,999,666))









# kwargs

def maek(**kwarge):
    # kwargs is the dictioinary with all the key value pair which were passed to marks
    for item in kwarge.keys():
        print(f"the mark of {item} is {kwarge[item]}")



maek(sujay=23,rajat=88,sumit=99)        





# Args and kwargs

def func1(*args,**kwargs):
    print(args)
    print(kwargs)


func1(7,8,9,5,5,6,sujay=99,sumit=88,rajat=252)  












def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(10, 20))
print(add(10, 20, 30, 40))
