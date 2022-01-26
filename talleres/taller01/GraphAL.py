from collections import deque

class Nodo:
    def __init__(self, valor, next = None):
        self.valor = valor
        self.next = next

class GraphAL:
    def __init__(self, size):
        self.arregloDeListas = [0]*size
        for i in range(0,size):
            self.arregloDeListas[i] = deque()
            
    def esta_vacia(self):
        return self.head == None #CONDICIONAL DEVUELVE BOOLEAN
        
    def addArc(self, vertex, destination, weight):
        fila = self.arregloDeListas[vertex]
        parejaDestinoPeso = (destination, weight)
        fila.append(parejaDestinoPeso)
        
    def getSuccessors(self, vertice):
        for i in range(0,vertice):
            successors = self.arregloDeListas
            return successors
            
    def getWeight(self, source, destination):
        for i in range(0,destination):
            weight = self.arregloDeListas
            return weight
