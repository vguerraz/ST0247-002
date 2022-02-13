program: main.o Graph.o Vertex.o
	g++ -o $@ main.o Graph.o Vertex.o

main.o: main.cpp Graph.o Vertex.o
	g++ -c $<

Graph.o: Graph.cpp Graph.h
	g++ -c $<

Vertex.o: Vertex.cpp Vertex.h
	g++ -c $<

clean:
	del programa *.o