# while loop define that loop is perform until the condition is not false



i=1 
while i<11:
    print(i)
    i=i+1



a=int(input("enter your number="))
while a in [1,2,3,6,5]:
    print("you won the game\nyour number is = ",a)
    break




#  infinte loop
# i=1
# while i<4:
#     print(i+1)




n = int(input("Enter your range: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
    