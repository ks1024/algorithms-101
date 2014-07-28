#! /usr/bin/env python
# -*- coding: utf-8 -*-

def kruskal(G):

    T = set()
    d = {}
    for v in G['vertices']:
        d[v] = set([v])

    new_edges = sorted(list(G['edges']), key=lambda edge: edge[2])
    #print d
    #print new_edges
    for e in new_edges:
        v1 = e[0]
        v2 = e[1]
        i = find_set(d, v1)
        j = find_set(d, v2)
        if i != j:
            union_set(d, i, j)
            T.add(e)
    print T

def find_set(d, vertex):
    for v, s in d.iteritems():
        if vertex in s:
            return v

def union_set(d, v1, v2):
    set1 = d[v1]
    set2 = d[v2]
    del d[v1]
    del d[v2]
    d[v1] = set1 | set2

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

    kruskal(G)
