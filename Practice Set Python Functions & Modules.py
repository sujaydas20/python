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
print((map(squere,lst)))
