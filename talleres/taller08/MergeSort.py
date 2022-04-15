def mergeSort(arreglo: list):
  return mergeSortAux(arreglo, 0, len(arreglo)-1)

def mergeSortAux(arreglo, inicial, final):
  if inicial == final:
    return
  else:
    mitad = (inicial  + final) // 2
    mergeSortAux(arreglo, inicial, mitad) #MergeIzq
    mergeSortAux(arreglo, mitad +1, final) #MergeIzq
    pegarLasDosMitades(arreglo, inicial, final)


def pegarLasDosMitades(arreglo,inicio, fin):
  mitad = (inicio + fin) // 2
  i= inicio
  j = mitad + 1 
  while i < j and j < len(arreglo):
    if arreglo[i] > arreglo[j]:
      arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
      j+=1
    else:
      i+=1
  return arreglo

def main():
  arreglo = [9, 8, 7, 6, 5, 4, 3, 2, 1]
  mergeSort(arreglo)
  print(arreglo)
  

#pegarLasDosMitades([2,8,3,5], 0)
main()
