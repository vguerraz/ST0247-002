class GraphAm:
    def __init__(self, size): #Los palitos indican que el método es privado.
      dimensiones = (size,size)
      self.matriz = np.zeros( dimensiones )    

    def getWeight(self, source, destination):
      return self.matriz[source][destination]

    def addArc(self, source, destination, weight):
    	self.matriz[source][destination] = weight

    def getSuccessors(self, vertex):
      filaVertice = self.matriz[vertex]
      respuesta = []
      for j in range(0,size):
        if filaVertice[j] != 0:
           respuesta.append(j)
      return respuesta


