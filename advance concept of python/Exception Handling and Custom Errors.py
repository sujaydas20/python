
# while True:
#     try:            

#         a=int(input("enter your number 1:  "))
#         b=int(input("enter your number2 :  "))
#         print(f"the sum of division is {a/b}")

#     except ValueError:
#         print("dont use another value")
#     except ZeroDivisionError:
#         print("please dont use the 0 ")        

#     except Exception as e:
#         print("erroe is found!\ncheck your input",e)


while True:
    a=int(input("enter your number 1:  "))
    b=int(input("enter your number2 :  ")) 


    if b==0:
        raise ValueError("sont use 0")
    print(f"the sum of division is {a/b}")

 