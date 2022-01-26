import sys
import numpy as np
class GraphAM:
    def __init__(self):
        self.matriz = ([[1,2,3],[3,4,5],[7,8,9]])
        np.set_printoptions(threshold=sys.maxsize)
        print(self.matriz)
    
    def getWeight(self, source, destination):
        return self.matriz[source][destination]
    
    def addArc(self, source, destination, weight):
        self.matriz[source][destination] = weight
    
    def getSuccessors(self, vertex):
        filaVertice = self.matriz[vertex]
        respuesta = []
        for j in range(0,len(self.matriz)):
            if filaVertice[j] != 0:
                respuesta.append(j)
                return respuesta
                
graph = GraphAM()
print(graph.getWeight(0,1))
graph.addArc(2,1,9)
print(graph)
