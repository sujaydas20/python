class Employe:


    def __init__(self,name,salary,bond):
        self.name=name
        self.salary=salary
        self.bond=bond


    def get_money(self):
        return self.salary
    
        # pass
    def get_info(self):
        print(f"the name is {self.name}\nsalary of the employe is {self.salary} RS\nthe bond of the comapny for {self.bond}years")

    
        
        # return 100000


e1=Employe('sujay',1000000,4)    
# print(e1.get_money())
e1.get_info()