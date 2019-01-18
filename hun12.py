a=[]
d=int(input())
b=int(input("enter the size: "))
for i in range(0,b):
c=input("enter the number: ")
a.append(c)
a.sort()
print(a)
rev=a[::-1]
ans=rev[d-1]
print(ans)
