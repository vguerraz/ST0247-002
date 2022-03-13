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

       
# This class represents a directed graph
# using adjacency matriz representation


class GraphAM:
    def __init__(self, size):
        self.__size__ = size
        self.__Array__=np.zeros((size,size))

    def addArc(self, vertex, edge, weight):
        self.__Array__[vertex][edge]=weight

    def getSuccessors(self, vertice):
        sucesor=deque()
        for i in range (0,self.__size__):
            if self.__Array__[vertice][i]!=0:
                sucesor.append(i)
        return sucesor

    def getWeight(self, source, destination):
        return self.__Array__[source][destination]#=============================================================================================)

                
# ------------ BFS -------------
# 1.We can select any vertex as started vertex.
# 2. Explorating the adjacents.

def my_BFS(graph, inicial_vertex):
  route = [inicial_vertex]
  count = 0
  explorate = route[count]
  while count != len(route):
    for i in graph.getSuccessors(explorate):
      if i not in route:
        route.append(i)
    count += 1
  return route



# ------------------------------------------------------------------------------------
size = 4
graph_list = GraphAL(size)
graph_matriz = GraphAM(size)

graph_list.addArc(0,1,3)
graph_list.addArc(0,2,4)
graph_list.addArc(0,3,10)
graph_list.addArc(1,0,7)
graph_list.addArc(1,3,1)
graph_list.addArc(1,2,6) 
graph_list.addArc(2,1,2)
graph_list.addArc(2,0,8)
graph_list.addArc(2,3,9)
graph_list.addArc(3,2,5)
graph_list.addArc(3,1,11)
graph_list.addArc(3,0,4)


graph_matriz.addArc(0,1,3)
graph_matriz.addArc(0,2,4)
graph_matriz.addArc(0,3,10)
graph_matriz.addArc(1,0,7)
graph_matriz.addArc(1,3,1)
graph_matriz.addArc(1,2,6) 
graph_matriz.addArc(2,1,2)
graph_matriz.addArc(2,0,8)
graph_matriz.addArc(2,3,9)
graph_matriz.addArc(3,2,5)
graph_matriz.addArc(3,1,11)
graph_matriz.addArc(3,0,4)

print(my_BFS(graph_list, 3))
print(my_BFS(graph_matriz, 3))
