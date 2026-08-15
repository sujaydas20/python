# while(data:=input("enter your nuber")):
#     print(data)
#     if (data) =="x":
#         print()
#         break      









total = 0

while (data := input("Enter your number (x to stop): ")):
    if data == "x":
        break

    total += int(data)

print("Total =", total)