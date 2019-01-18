
b=str(input())
b=b.lower()
g=len(b)
h=[]
for i in range(1,g+1):
h.append(b[-i])    
for i in h:
if i=='a':
 h.remove(i)
elif i=='e':
 h.remove(i)
  elif i=='i':
 h.remove(i)
 elif i=='o':
 h.remove(i)
 elif i=='u':
h.remove(i)
k="".join(h)
print(k)   
