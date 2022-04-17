import numpy as np

#Levenshtein distance - Recursion 

def levenshtein(A : str, B : str) -> int:
  return levenshteinAux(A,B,0,0) 


def levenshteinAux(A, B, i, j) -> int:
  if i == len(A) or j == len(B):
    return 0
  elif A[i] == B[j]:
    return  levenshteinAux(A,B,i+1,j+1)
  else:
    return 1 + min( levenshteinAux(A,B,i+1,j), levenshteinAux(A,B,i,j+1), levenshteinAux(A,B,i+1,j+1))


#Levenshtein distance - Dynamic programming

  #1. Creo la estructura de datos que va a representar el stack
  #2.Llenar la tabla

def levenshtein_DP(A:str, B:str ):
  n, m = len(A)+1 , len(B)+1 #Agrego Epsilon
  stack = np.zeros( (n,m) )
  
  for i in range(1,n):
    stack[i][0] = i
  for i in range(1,m):
    stack[0][i] = i    
  
  for i in range (1, n):
    for j in range (1, m):
      
      if A[i-1] == B[j-1]:
        stack[i][j] = stack[i-1][j-1] #No afecta
      else: 
       stack[i][j] = 1 + min(stack[i-1][j], stack[i][j-1],stack[i-1][j-1] )
  #print(stack)
  return stack [len(A)-1][len(B)-1]


def main():
  print(" --- RECURSION ---")
  print(levenshtein("abdace","babce"))
  print(levenshtein("benyam","ephrem"))
  print(levenshtein("casita","mamita"))
  print(" --- DYNAMIC  ---")
  print(levenshtein_DP("abdace","babce"))
  print(levenshtein_DP("benyam","ephrem"))
  print(levenshtein_DP("casita","mamita"))

main()
