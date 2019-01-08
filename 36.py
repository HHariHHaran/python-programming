 a = input("")
 s = sum(e.isspace() for e ina )
 w = sum(e.isalpha() for e in a)
 d = sum(e.isdigit() for e in a)
 sc= len(a)-w-s-d
print(sc)
