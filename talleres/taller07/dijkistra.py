from cmath import inf

def actualizarLaTabla(g,v,distancias, predecesores) -> None:
  losVecinosDeV = g.getSuccessors(v)
  for vecino in losVecinosDeV:
    elPesoDeVAlVecino = g.getWeight(v,vecino)
    if distancias[v] + elPesoDeVAlVecino < distancias[vecino]: 
      distancias[vecino] = distancias[v] + elPesoDeVAlVecino
      predecesores[vecino] = v

def elMasCercaQueNoEsteVisitado(g,v,visitados) -> int:
  losVecinosDeV = g.getSuccessors(v)
  elPesoDelMasCerca = inf
  elMasCerca = 0
  for vecino in losVecinosDeV:
    peso = g.getWeight(v,vecino)
    if peso <= elPesoDelMasCerca and not visitados[vecino]:
      elPesoDelMasCerca = peso
      elMasCerca = vecino
  return elMasCerca

def dijkstra(g,s : int) -> list:
  distancias =  [inf]*g.size()
  distancias[s] = 0
  predecesores = [-1]*g.size()
  visitados = [False]*g.size()
  visitados[s] = True
  v = s
  for _ in range(1,g.size()+1):
    v = elMasCercaQueNoEsteVisitado(g,v,visitados)
    visitados[v] = True
    actualizarLaTabla(g,v,distancias,predecesores)
  return distancias

