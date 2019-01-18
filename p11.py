h = input()
if(h in ["Saturday","SATURDAY","saturday","Sunday","sunday","SUNDAY"]):
print("yes")
elif(h in ["MONDAY","Monday","monday","TUESDAY","Tuesday","tuesday","WEDNESDAY","Wednesday","wednesday","THURSDAY","Thursday","thursday","FRIDAY","Friday","friday"]):
print("no")
else:
print("Invalid Input")
