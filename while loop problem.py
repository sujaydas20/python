
# sum the number
sum=0
i=0
while i<=100:
   print(i)
   sum +=i
   i+=1
print(sum)   

# find password until not type write on
pasword="suji"
entee_pasword=input("enter your pasword  = ")
while(entee_pasword!=pasword  ):
   entee_pasword=input("wrong password! try again an enter password = ")
print("success !your logd in = ")   



#  reversed number
num=44331
print(int(str(num)[::-1]))