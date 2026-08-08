# try:
#     a=452/5
# except Exception as e:
#     print(e)
# # it check there is no error
# else:
#     print("good no error")        












def divide(a,b):
    try:
        c=a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    # this is always excutedmno for outhers
    finally:
        print("this is always excuted")
a=int(input("enter your number 1:"))      
b=int(input("enter your number 2:"))   
divide(a,b)
