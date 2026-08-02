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



#  Read-Only Properties








class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):  # Read-only computed property
        return 3.1416 * self._radius * self._radius

c = Circle(5)
print(c.radius)  # 5
print(c.area)  # 78.54

# c.radius = 10  # Raises AttributeError: can't set attribute
# c.area = 20 # Raises AttributeError: can't set attribute