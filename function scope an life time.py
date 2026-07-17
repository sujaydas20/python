def sum (a,b): 
    # a na b are the local veriable
    c=a+b  
    z=1# it is a local veriable
    return c
def greet():
    z=25
    print("hello")

z=8#it is a golbal veriable
greet ()
print(sum(8,9))
print(z)








# global veriable
def sum(a,b):
    print("hey i am sujay")
    c=a+b
    global z
    z=0
    return c
z=3
print(sum(7,3))
print(z)