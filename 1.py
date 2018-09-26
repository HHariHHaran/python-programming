number = int(input("Enter any num: "))
flag = number%2
if flag == 0:
    print(number, "is an even num")
elif flag == 1:
    print(number, "is an odd num")
else:
    print("Error, Invalid input")
