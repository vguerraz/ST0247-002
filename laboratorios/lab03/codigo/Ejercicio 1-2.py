import numpy as np

def n_reinas(n:int):
  tablero = [0]*n
  return n_reinas_aux(n, 0, tablero)
  
def n_reinas_aux(n:int, c:int, tablero:list)->list:
  if c==n:
    return True
  else:
    for row in range(n):
      tablero[c] = row  #Empieze a probar
      if se_atacan_hastaI(tablero, c):
        pass
      else:
        if n_reinas_aux(n, c+1, tablero):
          return tablero

def se_atacan_hastaI(tablero: list, i:int):
  ataque = False
  for j in range(0,i):
    for k in range(j+1, i+1):
      if np.abs(tablero[j]-tablero[k]) == np.abs(j-k) or tablero[j]==tablero[k] :
        ataque = True
  return ataque
    
def main():
  n= int(input("Número de reinas: "))
  print(n_reinas(n))

main()
