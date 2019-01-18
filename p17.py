
try:
g = int(input())
d = int(input())
l=max(g,d)
m=l
p = min(g,d)
while(m%p!=0):
m+=l
print(m)    
except:
print("Invalid Input")
