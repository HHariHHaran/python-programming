number = int(input("Enter the value of n: "))
hold = number
sum = 1

if number <= 1: 
   print("Enter a whole positive num !") 
else: 
   while number > 1:
        sum = sum + number
        number = number -1
    print("Sum of first", hold, "natural numbers is: ", sum)
