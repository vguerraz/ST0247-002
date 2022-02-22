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
        
    def getWeight(self, source, dest)->int:   
      vertex = self.getSuccessors(source)
      for i in range(0, len(vertex)):
        if vertex[i][0]==dest:
          return vertex[i][1]
      return 0
      

    def getSuccessors(self, vertice):
      successors = self.arregloDeListas[vertice]
      return successors
      

def verificar_bien_pintado(colored, index, graph):
  for vertex in range(0, index+1):
    vertex_color = colored[vertex]
    for sucesor in graph.getSuccessors(vertex):
      if sucesor[0] <= index:
        sucesor_color = colored[sucesor[0]]
        if vertex_color == sucesor_color:
          return False
  return True

def pintar_con_M_colores(graph, m:int, size):
  return pintarAUX(graph, [0]*size, m , 0)

def pintarAUX(graph, color_list, m, vertex):
  if vertex == len(color_list):
    print (color_list)
    return True
  for color in range(0, m):
    color_list[vertex] = color
    if verificar_bien_pintado(color_list, vertex, graph):
      it_was_possible_to_coloring = pintarAUX(graph, color_list, m, vertex+1)
      if it_was_possible_to_coloring:
        return True
  return False
  


size = 7
graph = GraphAL(size)

#graph.addArc(0,0,3)
graph.addArc(0,2,4)
graph.addArc(0,1,10)
graph.addArc(1,2,1)
graph.addArc(1,5,1)
graph.addArc(2,1,6) 
graph.addArc(2,5,2)
graph.addArc(2,3,8)
graph.addArc(3,4,1)
graph.addArc(4,0,1)


'''print(graph.getSuccessors(0))
print(graph.getSuccessors(1))
print(graph.getSuccessors(2))
print(graph.getSuccessors(3))
print(graph.getSuccessors(4))
print(graph.getSuccessors(5))
print(graph.getSuccessors(6))'''

print(verificar_bien_pintado([1,3,2,1,3,2,1], 5, graph)) #False
print(pintar_con_M_colores(graph, 3, size))
