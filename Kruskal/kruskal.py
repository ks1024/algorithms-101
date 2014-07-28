#! /usr/bin/env python
# -*- coding: utf-8 -*-

def kruskal(G):

    MST = set()     # Create an empty set for the final minimum spanning tree
    F = {}          # Create an empty dictionary for storing tree sets => an empty forest
    
    # In the beginning, make a set(tree) for each vertex of G,
    # where each set(tree) is a single node tree
    for v in G['vertices']:    
        F[v] = set([v])

    # Sort the edges of G in ascending order
    edges = sorted(list(G['edges']), key=lambda edge: edge[2])
    
    for edge in edges:
        v1 = edge[0]    # Vertex 1
        v2 = edge[1]    # Vertex 2
        i = find_set(F, v1)  # Find index of tree of vertex
        j = find_set(F, v2)
        if i != j:      # If v1 and v2 belong to different sets
            union_set(F, i, j)
            MST.add(edge)
    
    return MST

def find_set(f, vertex):
    """Find which set(tree) the vertex belongs to
    
    f(forest) is a dict which key as index and value as set(tree)
    """
    for k, s in f.iteritems():
        if vertex in s:
            return k

def union_set(f, index1, index2):
    """Union the two different sets

    """
    set1 = f[index1]
    set2 = f[index2]
    del f[index1]
    del f[index2]
    f[index1] = set1 | set2

if __name__ == '__main__':

    G = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        'edges': set([
            ('A', 'B', 4),
            ('B', 'C', 10),
            ('A', 'F', 8),
            ('C', 'D', 3),
            ('B', 'F', 9),
            ('B', 'D', 12),
            ('B', 'G', 7),
            ('B', 'H', 3),
            ('G', 'H', 3),
            ('G', 'E', 6),
            ('H', 'E', 3),
            ('F', 'E', 7),
            ('E', 'D', 6),
            ('F', 'G', 4),
            ('D', 'H', 10)
        ])
    }

    edges = list(kruskal(G))
    for e in edges:
        print "Edge: ", e
