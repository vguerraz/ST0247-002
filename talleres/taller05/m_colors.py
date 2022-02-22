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
      

def verificar_bien_pintado(colored, index, graph):
  for vertex in range(0, index+1):
    vertex_color = colored[vertex]
    for sucesor in graph.getSuccessors(vertex):
      if sucesor[0] <= index:
        sucesor_color = colored[sucesor[0]]
        if vertex_color == sucesor_color:
          return False
  return True


def how_many_colors(graph, size):
  return how_many_colorsAUX(graph,[0]*size, 0)

def how_many_colorsAUX(graph, color_list, vertex, m_colors = 1):
  if vertex == len(color_list)-1:
    return m_colors

  else:
    for color in range(0, m_colors+1):
      color_list[vertex] = color
      if verificar_bien_pintado(color_list, vertex, graph):
        it_was_possible_to_coloring = how_many_colorsAUX(graph, color_list, m_colors, vertex+1)
        if it_was_possible_to_coloring:
          return m_colors + 1
        else:
          return how_many_colorsAUX(graph, [0]*size, 0, m_colors+1)
        


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

size2 = 1
graph2 = GraphAL(size)

size3 = 2
graph3 = GraphAL(size)
graph3.addArc(0,1,4)

size4 = 3
graph4 = GraphAL(size)
graph4.addArc(0,1,4)
graph4.addArc(1,2,4)
graph4.addArc(2,0,4)
graph4.addArc(0,2,4)
graph4.addArc(1,0,4)
graph4.addArc(2,1,4)

print(how_many_colors(graph2, size2)) #1
print(how_many_colors(graph3, size3)) #2
print(how_many_colors(graph4, size4)) #3
print(how_many_colors(graph, size)) #3
print(graph4.getSuccessors(0))
print(graph4.getSuccessors(1))
print(graph4.getSuccessors(2))
