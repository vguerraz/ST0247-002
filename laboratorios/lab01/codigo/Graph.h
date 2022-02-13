#ifndef graph_h
#define graph_h


#include <iostream>
#include <string>
#include <vector>
#include "Vertex.h"
#include <stdlib.h> //new - delete

using namespace std;
 
class Graph{
   private:
      const int MAX_VERTS = 20;
      int nVerts; // current number of vertices
      Vertex **vertex_list;
      float **adjMat; // adjacency matrix 
      
     
   public:
      Graph();
      ~Graph();
      
      
      void add_vertex(int i, string lab, float x, float y);
      void add_edge(Vertex* Vsource, Vertex* Vdestination, float weight);
      void set_nVerts(int nVerts);
      void set_vertexList(Vertex* ver, int pos);
      Vertex* get_vertexList(int pos);
      int get_nVerts();
      int what_is_my_vert(string label);
      void display_vertexList();
      void display_adjMat();

 
};

#endif