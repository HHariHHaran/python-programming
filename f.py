number1 = 20
number2 = 24
number3 = 22

if (number1 >= number2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3

print("The largest num between",number1,",",number2,"and",number3,"is",largest)
