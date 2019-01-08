b=[]
c=[]
n=int(input("n"))
for i in range(0,n):
 a=int(input("a"))
 b.append(a)
 c.append(sorted(b))
d=c[-1]
e=d[::-1]
for i in range(0,n):
print(e[i],end='')
