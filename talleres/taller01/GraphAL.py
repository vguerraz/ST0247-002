import numpy as np
from collections import deque #Libreria para Listas

class GraphAL:
    def __init__(self, size):
      self.arregloDeLista = [0]*size
      for i in range(0,size):
         arregloDeLista[i] = deque()

    def addArc(self, vertex, edge, weight):
        fila = self.arregloDeLista[vertex]
        parejaDestinoPeso = (destination, weight)
        fila.append(parejaDestinoPeso)  #appendleft para añadir al inicio.


    def getSuccessors(self, vertice):
        filaVertice = self.arregloDeLista[vertice]
      respuesta = []
      
      for j in range(0,size):
        if filaVertice[j] != 0:
           respuesta.append(j)
      return respuesta


    def getWeight(self, source, destination):
        return self.arregloDeLista[source][destination]


