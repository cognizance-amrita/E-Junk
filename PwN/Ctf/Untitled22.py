X = [[1,2],  
      [4,5],  
     [7,8]]  
  
Result = [[0,0,0],  
             [0,0,0]]  
  
# iterate through rows  
for i in range(len(X)):  
   for j in range(len(X[0])):  
       result[j][i] = X[i][j]  
  
for r in result:  
   print(r)  