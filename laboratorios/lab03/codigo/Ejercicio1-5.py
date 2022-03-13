from collections import deque
import numpy as np

# This class represents a directed graph
# using adjacency list representation

class GraphAL:
    def __init__(self, size):
      self.size = size
      self.arregloDeListas = [0]*size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]

      for i in range(0, size):
        self.arregloDeListas[i]= deque()
  
        
    def addArc(self, vertex, destination, weight):
       fila = self.arregloDeListas[vertex]
       arco = (destination,weight)
       fila.append(arco)
        
    def getWeight(self, source, dest):   
      vertex = self.getSuccessors(source)
      for i in range(0, len(vertex)):
        if vertex[i][0]==dest:
          return vertex[i][1]
      return 0
      

    def getSuccessors(self, vertice): 
      succesors = []
      for i in self.arregloDeListas[vertice]:
        succesors.append(i[0])
      return succesors

       
                
 # ----------------Review cycle  ----------------------------------------

def is_there_a_cycle(graph):
  cycle = False
  cycles = []
  for i in range (0, graph.size): 
    if i in graph.getSuccessors(i):
      cycle = True
      cycles.append(i)
  return (cycle, cycles)


# ------------------------------------------------------------------------------------
size = 4
graph_list = GraphAL(size)

graph_list.addArc(0,1,3)
graph_list.addArc(0,0,3)
graph_list.addArc(0,2,4)
graph_list.addArc(0,3,10)
graph_list.addArc(1,0,7)
graph_list.addArc(1,3,1)
graph_list.addArc(1,2,6) 
graph_list.addArc(2,1,2)
graph_list.addArc(2,0,8)
graph_list.addArc(2,3,9)
graph_list.addArc(3,2,5)
graph_list.addArc(3,3,5)
graph_list.addArc(3,1,11)
graph_list.addArc(3,0,4)



is_there_a_cycle(graph_list)
