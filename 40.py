n11 = 0
n12 = 1
count = 0
nterms=int(input("n"))
if nterms <= 0:
print("Positive integer")
elif nterms == 1:
print("Fibonacci sequence upto",nterms,":")
print(n11)
else:
print("Fibonacci sequence upto",nterms,":")
while count < nterms:
print(n11,end='  ')
 nth = n11 + n12
  n11 = n12
  n12 = nth
  count += 1
