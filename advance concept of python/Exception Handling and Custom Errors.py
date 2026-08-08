
while True:
    try:            

        a=int(input("enter your number 1:  "))
        b=int(input("enter your number2 :  "))
        print(f"the sum of {a+b}")

    except Exception as e:
        print("erroe is found!\ncheck your input",e)

    