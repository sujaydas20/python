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


# """




# decoraters with argument
def repeat(n):
    def decorater(func):
        def warpper(a):
            for i in range(n):
                func(a)

        return warpper
    return decorater
@repeat(7)
def say_hello(a):
    print(f"hello! {a}")
say_hello("sujay")    

"""
    it replace the function say_hello with this:
      def decoraters (func):
      def warpper(a)
          for i in range(n)
              say_hello(a)
        return warpper        
    
    
    
    
#     """
    # say_hello("sujay")



        
    # Decorator with argument
# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for i in range(n):
#                 func(a)
#         return wrapper
#     return decorator

# @repeat(7)
# def say_hello(a):
#     print(f"Hello! {a}")

# # Function call
# say_hello("Sujay")
    
    


