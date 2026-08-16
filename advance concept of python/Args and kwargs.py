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