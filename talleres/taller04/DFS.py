from collections import deque
import math

infinity = math.inf

class GraphAL:
    def __init__(self, size):
      self.arregloDeListas = [0]*size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]

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



def cost_of_shortest(graph,size,source:int,dest:int)->int:
  visited = [False]*size
  return cost_of_shortestAUX(graph,source,dest,visited)

def cost_of_shortestAUX(graph,source:int,dest:int,visited:list, shortest_cost = 1000000)->int:
  print("Source",source)
  print("Dest",dest)
  visited[source] = True
  if source == dest:
    print("Source",source)
    print("Dest",dest)
    return 0
  else:
    for nextVert in graph.getSuccessors(source):
      if not visited[nextVert[0]]:
        cost_of_shortest_past_my_nextVert = int(graph.getWeight(source,nextVert[0])) + int(cost_of_shortestAUX(graph,nextVert[0],dest,visited))
        
        if cost_of_shortest_past_my_nextVert < shortest_cost:
          shortest_cost = cost_of_shortest_past_my_nextVert
    visited[source] = False
    
    return shortest_cost
    


size = 7
graph = GraphAL(size)

graph.addArc(0,0,3)
graph.addArc(0,1,4)
graph.addArc(0,5,10)
graph.addArc(1,2,1)
graph.addArc(1,5,1)
graph.addArc(2,1,6) 
graph.addArc(2,5,2)
graph.addArc(2,3,8)
graph.addArc(3,4,1)
graph.addArc(4,0,1)
graph.addArc(4,5,3)

print(graph.arregloDeListas)
print("\n")
print(graph.getSuccessors(0))
print(graph.getSuccessors(4))
print(graph.getWeight(4,5)) #3
print(graph.getWeight(0,0)) #3
print(graph.getWeight(4,6)) #0
print(graph.getWeight(0,1)) #8

#print(cost_of_shortest(graph,size,0,0))#0
print(cost_of_shortest(graph,size,0,5))#4
