import numpy as np

def lcs_DP(A:str, B:str ):
  n, m = len(A) + 1 , len(B) + 1 #Agrego Epsilon
  stack = np.zeros( (n,m) )

  subsecuencia = ""
  
  for i in range (1, n):
    for j in range (1, m):
      
      if A[i-1] == B[j-1]:
        stack[i][j] = 1 + stack[i-1][j-1]

      else: 
       stack[i][j] = max(stack[i-1][j], stack[i][j-1])

  #Retornar la subsecuencia:
  i, j = n-1, m-1 
  while i is not 0 or j is not 0:
    if A[i-1] == B[j-1]:
      subsecuencia = A[i-1] + subsecuencia  
      i,j = i-1,j-1
    else:
      if i == 0:
        j = j-1
      elif j == 0:
        i = i-1
      else:
        maximo =  max(stack[i-1][j], stack[i][j-1] )
        if stack[i-1][j] == maximo:
          i,j = i-1,j
        else:  
          i,j = i,j-1

  return (stack[len(A)][len(B)], subsecuencia)


print(lcs_DP( "casita" , "mamita"))
print(lcs_DP( "ACEDF" , "CDASD"))
