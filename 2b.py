
N=int(input("number is="))
if(N<=0):
    print("invalid")
if(N<=1000):
    t=N
    rev=0
while N>0:
    re=N%10
    rev=rev*10+re
    N=N/10
if(t==rev):
    print("palindrom")
else:
    print("not palindrom")

