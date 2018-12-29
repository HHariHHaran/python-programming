l = int(input("Enter lower range: "))
u = int(input("Enter upper range: "))
if(l<=0):
 print "invalid"
if (u<=0):
print "invalid"
  for num in range(l,u+1):
     n = len(str(num))
      sum = 0
    temp = num
    while temp > 0:
      digit = temp % 10
       sum += digit ** n
       temp //= 10
        if num == sum:
         print(num)
   
    
