def decoraters(func):
    def warpper():
        print("i an about to excuted a function.........")
        func ()
        print("i have excute this finction............")
    return warpper
     
@decoraters
def say_hello():
    print("hello !")
say_hello()    
# f=decoraters(say_hello)
# f()


"""
f will look like this def f()
def f()
    print("i am about to excuted a functoin.....")
    print("hello")
    print("i have executed this function..........")


"""