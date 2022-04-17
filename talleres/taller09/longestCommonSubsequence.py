import numpy as np

#Longest common subsequence - Recursion

def lcs(A : str, B : str) -> int:
  return lcsAux(A,B,0,0) 


def lcsAux(A, B, i, j) -> int:
  if i == len(A) or j == len(B):
    return 0
  elif A[i] == B[j]:
    return 1 + lcsAux(A,B,i+1,j+1)
  else:
    return max( lcsAux(A,B,i+1,j), lcsAux(A,B,i,j+1))

def main():
  print(lcs("abdace","babce"))
  print(lcs("abcdefghij","ecdgi"))

main()

#Longest common subsequence - Dynamic programming

  #1. Creo la estructura de datos que va a representar el stack
  #2.Llenar la tabla

def lcs_DP(A:str, B:str ):
  n, m = len(A) + 1 , len(B) + 1 #Agrego Epsilon
  stack = np.zeros( (n,m) )
  
  for i in range (1, n):
    for j in range (1, m):
      
      if A[i-1] == B[j-1]:
        stack[i][j] = 1 + stack[i-1][j-1]
      else: 
       stack[i][j] = max(stack[i-1][j], stack[i][j-1])

  return stack[len(A)][len(B)]

print(lcs_DP( "casita" , "mamita"))
