 
def removeDuplicate(a, n): 
      
     
    index = 0
      
     
    for i in range(0, n): 
          
         
        for j in range(0, i + 1): 
            if (a[i] == a[j]): 
                break
        if (j == i): 
            a[index] = a[i] 
            index += 1
              
    return "".join(a[:index]) 
  

a= str(input("Enter the String"))
n = len(a) 
print(removeDuplicate(list(a), n)) 
