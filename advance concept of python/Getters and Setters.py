class employe:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def frist_name(self):
        l=self.name.split(" ")
        print(l)
        return l[0]
e= employe("sujay das",10000)
print(e.frist_name())    
