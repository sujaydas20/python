a=5
table=[]
for i in range(1,11):
    table.append(5*i)

print(table)    


# list comprehention

table=[5*i for i in range(1,11)]
print(f"list comprehention\n",table)