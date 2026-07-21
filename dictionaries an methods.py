sutend={"name":"sujay","age":"21","college":"pce nagpur"}
print(sutend,type(sutend))





mark = {
    'sujay': int(input("Enter Sujay's marks: ")),
    'sumit': int(input("Enter Sumit's marks: ")),
    'rajat': int(input("Enter Rajat's marks: "))
}

if mark["sujay"] >= 35:
    print("Sujay: Pass")
else:
    print("Sujay: Fail")

if mark["sumit"] >= 35:
    print("Sumit: Pass")
else:
    print("Sumit: Fail")

if mark["rajat"] >= 35:
    print("Rajat: Pass")
else:
    print("Rajat: Fail")



mark = {
    'sujay': int(input("Enter Sujay's marks: ")),
    'sumit': int(input("Enter Sumit's marks: ")),
    'rajat': int(input("Enter Rajat's marks: "))
}

for name, score in mark.items():
    if score >= 35:
        print(name, "Pass")
    else:
        print(name, "Fail")




