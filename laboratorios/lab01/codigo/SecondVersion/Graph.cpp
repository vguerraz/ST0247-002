#include "Graph.h"
      
Graph::Graph() {
   vertex_list = new Vertex*[nVerts];
   adjMat = new float*[nVerts];
   for (int i =0 ; i < nVerts; i++){
      adjMat[i] = new float[nVerts]; //Reservar espacio en la memoria para matriz N*N
   }
 } 

void Graph::set_nVerts(int nVerts){
  this->nVerts = nVerts;
}

int Graph::get_nVerts(){
  return this->nVerts;
}

void Graph::set_vertexList(Vertex* ver, int pos){
  this->vertex_list[pos] = ver;
}

Vertex* Graph::get_vertexList(int pos){
  return this->vertex_list[pos];
}

void Graph::add_vertex(int i, string lab, float x, float y){
  *vertex_list[i] = Vertex(lab, i, x, y);
}


void Graph::add_edge(Vertex* Vsource, Vertex* Vdestination, float weight){
   adjMat[Vsource->get_pos()][Vdestination->get_pos()] = weight;
   adjMat[Vdestination->get_pos()][Vsource->get_pos()] = weight;      
 }

void Graph::display_vertexList(){
  for (int i = 0; i < this->nVerts; i++){
    cout << vertex_list[i]->get_label() << "  ";
  } 
}

void Graph::display_adjMat(){
  for (int f = 0; f < this->nVerts; f++){
    for (int c = 0; c < this->nVerts; c++){
        cout << adjMat[f][c] << "      ";
    }
    cout << "\n";
  } 
}

