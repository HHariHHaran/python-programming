def d():
	s=input()
	d1=''
	c=1
	r=[]
	for i in range(len(s)-1):
	v=int(s[i])
	if v<26:
	d1=s[i]+s[i+1]
	if v>26:
continue
c=c+1
print(c)
try:
d()
except:
	print('invalid')
