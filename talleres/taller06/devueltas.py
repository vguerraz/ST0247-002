def devolver(denominaciones : list, cantidad : int):
  denominaciones.sort(reverse = True)
  print("Debe devolver: ")
  for denominacion in denominaciones:
    numeroDeMonedas = cantidad // denominacion
    cantidad = cantidad % denominacion
    print(str(numeroDeMonedas) + " monedas de " + str(denominacion))

def main():
  n = int(input("Valor a devolver "))
  devolver([500,300,200],n)

main()
