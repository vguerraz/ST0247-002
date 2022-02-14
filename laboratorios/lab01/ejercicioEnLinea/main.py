salida = "BICOLORABLE"

print("Ingrese el número de nodos")

n = int(input())

if n>200 or n<1:

  print("Excede el límite de nodos")

  

print("Ingrese el número de arcos")

arcos = int(input())

conexiones = []

print("Ingrese las conexiones del grafo")

for i in range (0, arcos):

  conexiones.append(list(map(int, input().split()))) ##Guarda todas las conexiones en una lista

print(conexiones)

color1 = [] 

color2 = []

for j in range (0, arcos):

  for k in range (0, 2):

    if conexiones[j][k] in color1:

      color1.remove(conexiones[j][k]) ##Si se repite un elemento en color1 entonces pasa a color2

      if conexiones[j][k] not in color2:

        color2.append(conexiones[j][k])

    else: 

      color1.append(conexiones [j][k])

for l in range (len(color1)):

  for m in range (len(color1)):

    if color1[l] < color1[m]:

      if [color1[l], color1[m]] in conexiones: ##Si los elementos de la misma lista se conectan

        salida = "NOT BICOLORABLE"

for l in range (len(color2)):

  for m in range (len(color2)):

    if color2[l] < color2[m]:

      if [color2[l], color2[m]] in conexiones: ##Si los elementos de la misma lista se conectan

        salida = "NOT BICOLORABLE"

  

print("color 1",color1)

print("color 2",color2)

print(salida)
