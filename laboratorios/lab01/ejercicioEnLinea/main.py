def clasificar(n, lista1, lista2, conexiones):
  for j in range(0, n):
    for k in range(0, 2):
      if conexiones[j][k] in lista1 or conexiones[j][k] in lista2:
        continue
      else:
        if k == 0:
          if conexiones[j][k+1] in lista1:
            lista2.append(conexiones[j][k])
          else:
            lista1.append(conexiones[j][k])
        else:
          if conexiones[j][k-1] in lista1:
            lista2.append(conexiones[j][k])
          else: 
            lista1.append(conexiones[j][k])

def ordenar(conexiones):
  for i in range(1,len(conexiones)):
    for j in range(0,len(conexiones)-i):
      if(conexiones[j+1][0]+conexiones[j+1][1] > conexiones[j][0]+conexiones[j][1]):
        aux=conexiones[j]
        conexiones[j]=conexiones[j+1]
        conexiones[j+1]=aux
  
def verificar(lista1, conexiones):
  for l in range(len(lista1)):
    for m in range(len(lista1)):
      if lista1[l] != lista1[m]:
        if [lista1[l], lista1[m]] in conexiones or [lista1[m], lista1[l]] in conexiones: 
          return False
      return True

def main():
  print("Ingrese el número de nodos")
  n = int(input())
  while n > 0 and n < 200:
    print("Ingrese el número de arcos")
    arcos = int(input())
    
    conexiones = []
    print("Ingrese las conexiones del grafo")
    for i in range(0, arcos):
      conexiones.append(list(map(int,input().split())))##Guarda todas las conexiones en una lista
    ordenar(conexiones)
    
    color1 = []
    color2 = []
    clasificar(arcos, color1, color2, conexiones)
    if (verificar(color1, conexiones) and verificar(color2, conexiones)) == True:
      print("BICOLORABLE")
    else:
      print("NOT BICOLORABLE")

    print("Ingrese el número de nodos")
    n = int(input())

main()
