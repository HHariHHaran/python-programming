n=raw_input("N:")
m=len(n)
c=0
I=1
V=5
X=10
for i in range(m):
if(n[i]=='I'):
c=c+1
elif(n[i]=='V'):
c=c+5
else:
c=c+10
print(c)
