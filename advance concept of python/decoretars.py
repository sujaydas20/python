def decoraters(func):
    def warpper():
        print("i an about to excuted a function.........")
        func ()
        print("i have excute this finction............")
    return warpper     

def say_hello():
    print("hello !")
# say_hello()    
f=decoraters(say_hello)
f()