


class animal:
    location='india'
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("animal sound")
class dog(animal):
    def speak(self):
        # super().speak()
        print("woof")

d= dog("bruno")
# a=animal("dog")
d.speak()            
print(d.location)

print("author:- sujay das")