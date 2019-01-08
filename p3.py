n=int(input("enter a number:"))
rv=0
if(n>0):
 while n>0:
 rm=n%10
 rv=rv*10+rm
 n=n//10
 print("the number is:",rv)
else:
print "invalid"
