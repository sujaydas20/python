class employee:
    company ="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e=employee("sujay",150000)        
print(e.name,e.salary)