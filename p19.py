a=int(input())
l=list(1 for i in range(a))
li=[]
for i in range(2,a,1):
if l[i]==1:
for j in range(i*i,a,i):
l[j]=0
if a%i==0:
li.append(i)
print(" ".join(str(x) for x in li))
