class employee:
    company ="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):   #this is dunder method in python
        return f"the name is {self.name}an the salary is {self.salary}"    
    def __repr__(self):
        return f"name:{self.name }\n"
e=employee("sujay",150000)        
print(e.name,e.salary)

print(str(e))


print("sujauy")