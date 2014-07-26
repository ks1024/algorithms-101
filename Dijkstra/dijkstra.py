#! /usr/bin/env python
from collections import defaultdict

class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, edge, distance):
        node1 = list(edge)[0]
        node2 = list(edge)[1]
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)
        self.distances[(node1, node2)] = distance
        self.distances[(node2, node1)] = distance

def dijkstra(G, s):
    """Dijkstra algorithm:
    function Dijkstra(Graph, source)
        dist[source] := 0
        for each vertex in Graph:
            if v != source:
                dist[v] := infinity
                previous[v] := undefined
            end if
            add v to Q
        end for
        
        while Q is not empty:
            u := vertex in Q with min dist[u]
            remove u from Q
            
            for each neighbor v of u:
                alt := dist[u] + weight(u, v)
                if alt < dist[v]:
                    dist[v] := alt
                    previous[v] := u
                end if
            end for
        end while
        return dist[], previous[]
    end function
    """

graph = Graph()
nodes = 'ABCDEFGH'
for n in nodes:
    graph.add_node(n)

graph.add_edge('AB', 4)
graph.add_edge('BC', 10)
graph.add_edge('CD', 3)
graph.add_edge('DE', 6)
graph.add_edge('EF', 7)
graph.add_edge('FA', 8)
graph.add_edge('BF', 9)
graph.add_edge('BG', 7)
graph.add_edge('BH', 3)
graph.add_edge('BD', 12)
graph.add_edge('FG', 4)
graph.add_edge('GH', 3)
graph.add_edge('HD', 10)
graph.add_edge('GE', 6)
graph.add_edge('HE', 3)

print graph.nodes
print graph.edges.items()
print graph.distances
