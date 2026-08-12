def greater_than_9(x):
    if x>9:
        return True
    else:
        return False


a=[1,3,4,5,6,55,268,58,9,55,66,99,77,100,2225]    
new=  list(filter(greater_than_9,a))
print(new)






# def greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False


a=[1,3,4,5,6,55,268,58,9,55,66,99,77,100,2225]    
new=  list(filter(lambda x:x>9,a))
print(new)