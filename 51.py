b=1
c=1
g=[]
a=int(input("enter the no"))
v=len(str(a))
c=a
while(a>0):
 b=a%10
 a=a//10
 g.append(b)
for i in range(v-1,-1,-1):
 print(g[i],end=' ')
