b=[]
n=int(input("n"))
for i in range(0,n):
  a=int(input("a"))
b.append(a)
for i in range(1,100000):
 if((b.count(i))>1):
   print(i)
 else:
 print("the no is unique")
  break
