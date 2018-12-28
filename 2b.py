a=int(input("Enter number:"))
temp=a
rev=0
while(n>0):
    dig=a%10
    rev=rev*10+dig
    a=n
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
