def busquedaBinaria(arreglo : list, valor: int):
  return busquedaBinariaAux(arreglo, valor, 0, len(arreglo)-1)


def busquedaBinariaAux(arreglo : list, valor : int, inicio : int, fin):
  mitad = (inicio + fin) // 2

  if fin < inicio:
    return False

  if valor == arreglo[mitad]:
    return mitad

  if valor < arreglo[mitad]:
    return busquedaBinariaAux(arreglo, valor, inicio, mitad-1)

  if valor > arreglo[mitad]:
    return busquedaBinariaAux(arreglo, valor, mitad+1, fin)

#Complejidad: 0(log2 n)


def main():
  arreglo = [10, 20, 30, 40, 50, 60, 70, 80]
  print(busquedaBinaria(arreglo,10))
  print(busquedaBinaria(arreglo,80))
  print(busquedaBinaria(arreglo,40))
  print(busquedaBinaria(arreglo,0))
  print(busquedaBinaria(arreglo,90))
  print(busquedaBinaria(arreglo,41))

main()
