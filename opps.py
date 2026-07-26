"""
class

Abstraction:
Encapsulation:
Inheritance:
Polymorphism:
"""


# class an object
"""
Class: Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.

Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.

"""
# class employe:
#     company='asus'
#     def get_salary(self):
#         return 40000
# e=employe()
# print(e.get_salary())
# print(e.company)




# constructoe

class employe:

    def __init__(self , name , slary , bond):
     self.name=name
     self.slary=slary
     self.bond=bond
    

     def get_salary(self):
        return self.slary

    def get_info(self):
         print(f"the name of the employe id {self.name}. salary is {self.slary}. the bond is {self.bond} years")

e1=employe('sujay',400000,4)
# print(e1.get_slary())
e1.get_info()




