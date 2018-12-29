a=int(input("enter the first interval"))
b=int(input("enter the second interval"))
for j in range(a, b+1):
for i in range(2, j):
if(j%i)==0:
break
else:
print(j)
