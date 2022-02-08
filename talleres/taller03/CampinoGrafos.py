from collections import deque

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
        
    def getWeight(self, source, destination):   
      return self.arregloDeListas[source][destination] 

    def getSuccessors(self, vertice):
      successors = self.arregloDeListas[vertice-1]
      return  successors

    def hayCamino(self, graph, o:int, d:int)->bool:
      if o==d:
        return True
      else:
        for vecino in graph.getSuccessors(o):
          hayCaminoDelVecinoAd = graph.hayCamino(g,vecino,d)
          if hayCaminoDelVecinoAd:
            return True
      return False


    #def hay_camino_DFS(vertex:int , adjancency_list : deque, visited = []):
     # visited[vertex] = True  #Visited vertex
      #for neigthboor in  range(len(adjancency_list)):



      

size = int(input("Número de vértices del grafo:"))
n_edges =int(input("Número de aristas del grafo:")) 
graph = GraphAL(size)



for i in range (n_edges):
  source = int(input("Origen: ")) 
  destination = int(input("Destino: "))
  weight = int(input("Peso: "))

  graph.addArc(source, destination, weight)

print("Verify if there is path from A to B")
A = int(input("A: "))
B = int(input("B: "))
print(graph.hayCamino(graph.arregloDeListas, A, B))
