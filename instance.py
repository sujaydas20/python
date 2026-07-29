class Employe:
    company='asus'

    def __init__(self,name,salary,bond,company):
        self.name=name
        self.salary=salary
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"the name of the employe if {self.name}.\n salary is\n{self.salary}the bond if for\n{self.bond}years")   

e1=Employe ("sujay",100000,4,"hero")
print(e1.company)
print(Employe.company) 
print(e1)      