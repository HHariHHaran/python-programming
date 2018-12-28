m=int(input("Enter number:"))
temp=m
rev=0
while(n>0):
    dig=m%10
    rev=rev*10+dig
    m=n
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
