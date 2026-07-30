class car:
    def drive(self):
        print("car is moveing")
car1=car()
car1.drive()




# construction
class  person:
    def __init__(self,name,age):

        self.name=name
        self.age=age
p1=person('sujay',21)
print(p1.name,p1.age)