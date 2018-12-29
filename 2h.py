n=int(input("Enter number: "))
p=list(map(int,str(n)))
q=list(map(lambda x:x**3,p))
if(sum(q)==n):
print("The number is an armstrong number. ")
else:
print("The number isn't an arsmtrong number. ")
