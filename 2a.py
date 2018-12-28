
def powers(base,exp):
if(exp==2):
return(base)
if(exp!=2):
return(base*powers(base,exp-2))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",powers(base,exp))
