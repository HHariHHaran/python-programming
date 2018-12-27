year = int(input("Enter Year: "))
if year % 2 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 200 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
