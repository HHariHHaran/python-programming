p Nminelements(list1, U): 
    final_list =[]; 
   
    for i in range(0, U):     
        min1 = 9999999; 
           
        for j in range(len(list1)):       
            if list1[j]<min1: 
       min1 = list1[j]; 
   list1.remove(min1); 
 final_list.append(min1) 
 print(final_list) 
list1 = [4, 78, 34, 10, 8, 21, 11, 231]; 
U = 2; 
Nminelements(list1, U) 
