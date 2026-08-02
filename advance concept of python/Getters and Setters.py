class employe:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def frist_name(self):
        l=self.name.split(" ")
        # print(l)
        return l[0]
e= employe("sujay das",10000)
print(e.frist_name())    

















# Using @property (Pythonic Approach)

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, new_name):  # Setter
        self._name = new_name 

p = Person("Alice")
print(p.name)  # Alice (calls the getter)

p.name = "Bob"  # Calls the setter
print(p.name)  # Bob
 