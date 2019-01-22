
def round( a ): 
n = (a // 7) * 7
b = n + 7
   return (b if a - n > b - a else n) 
a = 4722
    print(round(a)) 
  
