# print("sujay is great")
class employee:
    company ='hp'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
# instance method 
    def print_info(self):
        info=f"the name is {self.name} and the salary is {self.salary}"
        print(info)
    @staticmethod
    def sum(a,b):
        return a+b
# class method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        # print(cls.company)   


         

        
    
e1=employee("sujay",150000)
e2=employee("durgesh",78000)
# print(employee.campany)
# print(employee.name)give the error 
# e1.print_info()
# e2.print_info()
# print(e2.sum(5,25)
# e1.print_company()

# employee.print_company()
# e1.print_company()
print(employee.company)
e1.change_company("asus")
# e1.print_company()

print(employee.company)









# class method


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))  # Creates a new Person instance

p = Person.from_string("Alice-30")
print(p.name, p.age)  # Alice 30