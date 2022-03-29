from collections import deque
import math

class GraphAL:
  def __init__(self, size): 
    self.siz = size
    self.arregloDeListas = [0]*size
    for i in range(0, size):
      self.arregloDeListas[i]= deque()
  
  def addArc(self, vertex, destination, weight):
    fila = self.arregloDeListas[vertex]
    arco = (destination,weight)
    fila.append(arco)
        
  def getWeight(self, source, dest)->int:
    vertex = self.getSuccessors(source)
    for i in range(0, len(vertex)):
      if vertex[i][0]==dest:
        return vertex[i][1]
    return 0 
    
  def getSuccessors(self, vertice):
    successors = self.arregloDeListas[vertice]
    return successors

def recorrer(graph : GraphAL):
  costo = 0
  elMasCerca = 0
  recorrido = []
  recorrido.append(elMasCerca)
  for vez in range(0,graph.siz):
    menorEncontrado = math.inf
    for siguiente in graph.getSuccessors(elMasCerca):
      peso_actual = siguiente[1]
      if peso_actual<menorEncontrado and siguiente[0] not in recorrido: 
        menorEncontrado = peso_actual
        elMasCerca = siguiente[0]
    recorrido.append(elMasCerca)
    costo = costo + menorEncontrado
    if len(recorrido) == graph.siz:
      costo = costo + graph.getWeight(recorrido[-1], recorrido[0])
      print("El recorrido propuesto es: ", recorrido)
      print("Y tiene un costo de: ",costo)
      break

graph = GraphAL(5)
graph.addArc(0,1,10)
graph.addArc(0,3,14)
graph.addArc(0,4,10)
graph.addArc(1,0,10)
graph.addArc(1,2,7)
graph.addArc(1,3,12)
graph.addArc(1,4,15)
graph.addArc(2,1,7)
graph.addArc(2,3,20)
graph.addArc(3,0,14)
graph.addArc(3,1,12)
graph.addArc(3,2,20)
graph.addArc(3,4,8)
graph.addArc(4,0,10)
graph.addArc(4,1,15)
graph.addArc(4,3,8)
recorrer(graph)
