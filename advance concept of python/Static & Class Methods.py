# print("sujay is great")
class employee:
    campany ='hp'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
# instance method 
    def print_info(self):
        info=f"the name is {self.name} and the salary is {self.salary}"
        print(info)

e1=employee("sujay",1500000)
e2=employee("durgesh",78000)
print(employee.campany)
# print(employee.name)give the error 
e1.print_info()
e2.print_info()

