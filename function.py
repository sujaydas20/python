def avg_(a,b):
    d=(a+b)/2
    print(d)
# avg_(2,3)    


# def agv(a,c):
#     d=(a+c)*9
#     return d
# o1=agv(1,2,)
# o2=agv(2,5,)


# print(o1)
# print(o2)




# def value_(a=int(input("enter your number= ")),b=int(input("enter ypur number= "))):
#     d=(a*b)
#     return d

# c =value_()
# print(c)
# # c1=value_(a,b=)




def number_(num):
    value=list(set(num))
    value.sort()
    return value[-2]
num=[1,2,5,6,4]
print (number_(num))
