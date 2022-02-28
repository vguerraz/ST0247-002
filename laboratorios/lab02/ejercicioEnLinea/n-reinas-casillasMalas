import numpy as np

def permutacionesSR(cadena):
  lista = []
  permutacionesSRAux(cadena,"", lista)
  print(len(lista))
  return lista

def permutacionesSRAux(pregunta, respuesta, lista):
  if len(pregunta)==0:
    if(nreinasValidas(respuesta)):
      lista.append(respuesta)
  else:
    for i in range(0,len(pregunta)):
      nuevaPregunta = pregunta[0:i]+pregunta[i+1:]
      permutacionesSRAux(nuevaPregunta , respuesta+pregunta[i], lista)

def nreinas(n : int):
  posiciones = ""
  for i in range (0, n):
    posiciones = posiciones+str(i)
  return permutacionesSR(posiciones)

def nreinasValidas(posible):
  for i in range (0, len(posible)):
    for j in range (i+1, len(posible)):
      x = int(posible[i])
      y = int(posible[j])
      if np.abs(j-i) == np.abs(y-x):
        return False
  return True

def casillasMalas(n):
  lista_casillas_malas = []
  for i in range(0, n):
    fila = input("Ingrese la fila")
    for j in range (len(fila)):
      if fila[j] == "*":
        lista_casillas_malas.append((j,i))
        #(columna, fila)
        #(posición, valor)
  return lista_casillas_malas
    
def verificarPosiciones (malas:list, reinas:list):
  validas = []
  for k in range (0, len(reinas)):
    tablero = reinas[k]
    for i in range(0, len(tablero)):
      for j in range(0, len(malas)):
        posicion = malas[j][0]
        valor = malas[j][1]
        if tablero[posicion]!=valor:
          validas.append(tablero)
          pass
  return validas

n = int(input("Número de reinas: "))
reinas = nreinas(n)
malas = casillasMalas(n)
print(reinas)
print(malas)

print(verificarPosiciones(malas, reinas))
