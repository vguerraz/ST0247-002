def rutas(mañana : list, tarde : list, limite : int, valor : int):
  mañana.sort()
  tarde.sort()
  horasextra = 0
  for i in range (0, len(mañana)):
    tiempo = max(mañana)+min(tarde)
    horasextra += (tiempo-limite)
    mañana.remove(max(mañana))
    tarde.remove(min(tarde))

  valorAPagar = horasextra * valor
  return valorAPagar


def main():
  l1 = list(map(int,input().split())) #linea 1 de entrada
  while (len(l1) == 3) and (l1 != [0, 0, 0]):
    mañana = list(map(int,input().split())) #línea 2, horarios mañana
    tarde = list(map(int,input().split())) #linea 3, horarios tarde
    print(rutas(mañana, tarde, l1[1], l1[2]))
    l1 = list(map(int,input().split())) #linea 1 de entrada

main()
