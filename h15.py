a=[]
n=int(input("enter the input:"))
for i in range(1,n+1):
c=int(input("N:"))
a.append(c)
a.sort(reverse=True)
for elem in a:
print elem
