s1=raw_input("input1:")
s2=raw_input("input2:")
a=0
b=0
if(len(s1),len(s2)<=100000):
for a in range(len(s1)):
if(s1[a]!=s2[a]):
b=b+1
if(b==1):
print "Yes"
else:
print "No"
else:
print "invalid"
