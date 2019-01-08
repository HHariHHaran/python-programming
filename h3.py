b=[]
c=[]

n=int(input("n"))
if(1<=n<=100000):
    d = 0
    for i in range(0,n):
        a=int(input("a"))
        b.append(a)
        if(i==b[i]):
        if(i>1):
       c.append(i)
        d=d+1
    if(d>0):
     for i in range(0,d):
     print(c[i],end='')
    else:
     print(-1)
