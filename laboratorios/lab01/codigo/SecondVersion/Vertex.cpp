#include "Vertex.h"

Vertex::Vertex(string lab, int pos, float x, float y) {
      this->label = lab;
      this->pos = pos;
      this->x=x;
      this->y=y;
      }

int Vertex::get_pos(){
      return this->pos;
}

string Vertex::get_label(){
      return this->label;
}