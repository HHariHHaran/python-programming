def compare(stra,strb):
for i in range(len(strb)):
stra+=strb[i]
print(stra)
def main():
try:
	sa=input()
  sb=input()
	compare(sa,sb)
except:
print('nvalid')
main()
