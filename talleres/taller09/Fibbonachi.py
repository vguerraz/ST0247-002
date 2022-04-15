#Fibbinnachi recursivo: Complejidad O(2**n)

def f(n):
  if n <= 1:
    return 1
  else:
    return f(n-1) + f(n-2)


#Fibbinnachi recursivo: Complejidad O(n)

def f_cycle(n):
  array = [0]*(n+1) #Stack
  array[0] = 1 
  array[1] = 1 # Condición de parada

  for i in range (2, len(array)):
    array[i] = array[i-1] + array[i-2]
  
  return array

print(f(4))
f_cycle(4)
