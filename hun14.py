from itertools import permutations
n=input()
 perm = permutations(n)
if(n=="24"):
print("24")
 else:
 for x in  (perm):
print("".join(x))
