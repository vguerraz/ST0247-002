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

#Generate possibles paths that goes to only one vertex (PERMUTATION WITHOUT REPETITION)
def possible_paths(nodes):
  paths = []
  possible_paths_aux(nodes,"", paths)
  return paths

def possible_paths_aux(question, answer, paths):
  if len(question)== 0:
    paths.append(answer)
  else:
    for i in range (0, len(question)):
      new_question = question[0:i] + question[i+1:]
      possible_paths_aux(new_question, answer+question[i], paths)

def generate_cycles(paths_brute_force:list):
  new_list = []
  for i in range (0, len(paths_brute_force)):
    cadena = paths_brute_force[i] + paths_brute_force[i][0]
    new_list.append(cadena)
  return new_list
  


def valid_paths(options:list, graph):
  lista = []
  for i in range (len(options)):
    for j in range (len(options[i])-1):
      for k in graph.getSuccessors(int(options[i][j])):
        if int(options[i][j+1]) == k[0]:
          if options[i] not in lista:
            lista.append(options[i])
          break
        elif options[i] in lista and k == graph.getSuccessors(int(options[i][j]))[-1]:
            lista.remove(options[i])
            break
      if options[i] not in lista:
        break
  return lista
  

def lowest_cost(valid_paths:list, graph):
  lowest = 99999999999999
  for i in range (0, len(valid_paths)):
    weight = 0
    for j in range (0, len(valid_paths[i])-1):
      weight += graph.getWeight(int(valid_paths[i][j]), int(valid_paths[i][j+1]))
    if weight < lowest:
      lowest = weight
  return lowest  

size = 5
graph = GraphAL(size)

graph.addArc(0,1,10)
graph.addArc(0,3,14)
graph.addArc(0,4,10)
graph.addArc(1,0,10)
graph.addArc(1,4,15) 
graph.addArc(1,3,12)
graph.addArc(1,2,7)
graph.addArc(2,1,7)
graph.addArc(2,3,20)
graph.addArc(3,2,20)
graph.addArc(3,0,14)
graph.addArc(3,1,12)
graph.addArc(3,4,8)
graph.addArc(4,3,8)
graph.addArc(4,1,15)
graph.addArc(4,0,10)

paths_brute_force = possible_paths("01234")
cycles = generate_cycles(paths_brute_force)
valid_cycles = valid_paths(cycles, graph)

print(valid_cycles)
print("The lowest cost of the cycle-path that visits each vertex only once is:", lowest_cost(valid_cycles, graph))
