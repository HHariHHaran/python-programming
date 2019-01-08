
a=int(input("Enter the no :"))
b=int(input("Enter the digit to delete :"))
if(1<=a<=1000000000000000000):
 c=str(a)[::-1]
 d=int(c)//(10**b)
print(str(d)[::-1])
else:
print("limit is exist")
