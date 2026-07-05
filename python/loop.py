# if else condtion
# the conditon is define that 
# if condition:-the code is execute when the condition is true
# elif :- code is  excute when 2nd condition is true 
# else :-  the code is execute when all condition  are false


age = int(input("enter the number = "))

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
elif age==0:
    print("abhi paida huaa hai tu chalna shikh le pahle")    
else:
    print("You are an adult.")
