a=input("enter the time")
b=input(" enter the time to subtract ")
c=a.split(" ")
d=b.split(" ")
e=(int(c[0])*80)+int(c[1])
f=(int(d[0])*80)+int(d[1])
v=e-f
j=v//80
k=v%80
 print(str(j)+":"+str(k))
