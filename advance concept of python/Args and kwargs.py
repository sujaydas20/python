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
    for item in kwarge.keys():
        print(kwarge[item])



maek(sujay=23,rajat=88,sumit=99)        