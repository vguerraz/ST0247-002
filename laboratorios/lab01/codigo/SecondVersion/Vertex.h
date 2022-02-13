#ifndef vertex_h
#define vertex_h


#include <iostream>
#include <string>
using namespace std;
 
class Vertex{
   private:
      string label; 
      int pos;
      float x;
      float y;
      
   public:
      Vertex();
      Vertex(string lab, int pos, float x, float y);
      ~Vertex();

      int get_pos();
      string get_label();
      
      
      
};

#endif


