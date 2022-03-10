from cmath import inf
from collections import deque
class GraphAL:
    def __init__(self, size):
        self.size=size
        self.arregloDeListas = [0]*size # = [0,0,0,0...]      
        for i in range(size):
            self.arregloDeListas[i] = deque()

    def addArc(self, source, destination, weight):
        laListaLlegada = self.arregloDeListas[source]
        unaPareja = (destination,weight)
        laListaLlegada.append(unaPareja)

    def getWeight(self, source, destination):
        laListaLlegada = self.arregloDeListas[source]
        for i in range(len(laListaLlegada)):
            pareja = laListaLlegada[i] # O(n)       
            theDestination = pareja[0]
            theWeight = pareja[1]
            if theDestination == destination:
                return theWeight      
        for (theDestination,theWeight) in laListaLlegada:
            if theDestination == destination:
                return theWeight      
        return 0    
    def getSuccessors(self, source):
        otraListica = deque()
        laListaLlegada = self.arregloDeListas[source]
        for (theDestination,theWeight) in laListaLlegada:
            otraListica.append(theDestination) 
        return otraListica   

def CaminoCercano(grafo):
    pesoMenor=inf
    pesoTotal=0
    visitado=[False]*grafo.size
    cercano=0
    verticeCandidato = 0
    for _ in range(grafo.size-1):
        pesoMenor=inf
        visitado[cercano]=True
        for sucesor in grafo.getSuccessors(cercano):
            peso = grafo.getWeight(cercano,sucesor)
            if peso<pesoMenor and not visitado[sucesor]:
                pesoMenor=peso
                verticeCandidato=sucesor
        cercano=verticeCandidato
        pesoTotal+=pesoMenor
    pesoTotal+=grafo.getWeight(cercano,0)
    return pesoTotal
