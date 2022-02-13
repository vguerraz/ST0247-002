#include "Vertex.h"
#include "Graph.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[]){
    Graph* my_graph = new Graph();
    if(argc==1){
        cout << "Any file has been entered by terminal";
    }
    else{
        string fileName, line;
        fileName=argv[1];
        fstream file;
        file.open(fileName);
        if(!file){
            cout<<"File "<< fileName <<" does not exist";
        }else{
            while(!file.eof()){
                getline(file,line);

                string coorX, coorY, label;
                float distance;
                int x = 0;
                bool nuevo = true;
                while(my_graph->get_vertexList(x)){
                    if(my_graph->get_vertexList(x)->get_label() == label){
                nuevo=false;
                break;
                }else{
                    x++;
                }
             }
                if (nuevo){
                    if (x=0){
                    x = -1;
                    }
                Vertex* verSource = new Vertex(label, x+1, 0, 0);
                my_graph->set_vertexList(verSource,x+1 );
                cout << "Se ha añadido el vertice " << label;
            }
        }   
        
    }  
    
    }
    my_graph->display_vertexList();
    my_graph->display_adjMat();

   return 0;    
    }
        


 
