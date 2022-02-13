#include "Vertex.h"
#include "Graph.h"
int main(int argc, char* argv[]){ 
    
    Graph* my_graph = new Graph();
    int nVert, nEdge;
    cout << "Number of vertices: ";
    cin >> nVert;
    my_graph->set_nVerts(nVert);
    cout << "Number of edges: ";
    cin >> nEdge;



    for (int i = 0; i < nEdge;i++){
        string source, destination;
        float distance;
        cout << "Source: "; 
        cin >> source;
        
        int x = 0;
        bool nuevo = true;
        while(my_graph->get_vertexList(x)){
            if(my_graph->get_vertexList(x)->get_label() == source){
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
            Vertex* verSource = new Vertex(source, x+1, 0, 0);
            my_graph->set_vertexList(verSource,x+1 );
            cout << "Se ha añadido el vertice " << source;
            }
            
        
        cout << "Destination: "; 
        cin >> destination;
        int y = 0;
        bool nuevo2 = true;
        while(my_graph->get_vertexList(x)){
            if(my_graph->get_vertexList(x)->get_label() == destination){
                nuevo2=false;
                break;
                }else{
                    y++;
                }
            }
        if (nuevo2){
            Vertex* verDest = new Vertex(source, y+1, 0, 0);
            my_graph->set_vertexList(verDest,y+1 );
            cout << "Se ha añadido el vertice " << destination;
            }

        cout << "Distance: "; 
        cin >> distance;
        my_graph->add_edge(my_graph->get_vertexList(x+1), my_graph->get_vertexList(y+1) , distance);
        }

    my_graph->display_vertexList();
    my_graph->display_adjMat();

   return 0;    
    }
        


 
