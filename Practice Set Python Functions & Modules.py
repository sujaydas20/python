def preent():
    print("hello python learner")
preent()    



def squer(x):
    return (x*x)
print(squer(4))



def name (frist,second):
    return f"{frist}{second}"
print(name("sujay","das"))



# check the area of the rectangle
def area(lenth,breath):
    return lenth*breath
print(f"the area of a rectangle is {area(70,80)}")




#lamda function


add= lambda a,b:a+b

print(add(5,5))


squere=lambda x:x*x
lst=[1,2,3,4]
print(list(map(squere,lst)))








# factorial of number
def factorial(n):
    if n==0 or n==1:

       return n
    return factorial(n-1)*n
print(factorial(5))



# sum of digit

def sum(n):
    if n==0:
        return 0
    return n%10 + sum(n//10)
# 7896
# 2+sum(7896)
print(sum(7854))





# pip module

import math
a= math.sqrt(144)
b= math. sin( math.radians(90))
print(a,b)

# import requests
# a=requests.get("https://github.com/MoreshwarPachbhai")
# print(a.json())

# import requests

# a = requests.get("https://github.com/MoreshwarPachbhai")

# print(a.status_code)
# print(a.text[:300])   # Print the first 300 characters

# import requests

# a = requests.get("https://www.instagram.com/maisamayhoon?igsh=MWIzenYzanZzNXdybA==")

# print(a.status_code)
# print(a.json())



def incre():
    counter = 0
    counter +=1
    print(counter) 


incre()
incre()    
incre()    
incre()        
