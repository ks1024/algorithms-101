# Kruskal's Minimum Spanning Tree

## Example
![img](https://raw.github.com/yankuangshi/algorithms-training/master/Kruskal/img/mst_example.png)

## Algorithm

* We create a dictionary containing |V| trees (sets), where each tree has only one node.
![img](https://raw.github.com/yankuangshi/algorithms-training/master/Kruskal/img/screenshot1.png)

* So in the beginning, we have a forest of single node tree.
![img](https://raw.github.com/yankuangshi/algorithms-training/master/Kruskal/img/screenshot2.png)

* Sorting the edges in ascending order.

```
BH => 3
CD => 3
EH => 3
GH => 3
AB => 4
...
DH => 10
BD => 12
```

* We starting add edges and check whether the two vertices of the edges belong to a different trees. Because if the two vertices belong to a same tree, it makes a circle when the edge is added to.

* At some monent, we will have a forest of "n" (which n < |V|) trees, which are all a sub-trees of the minimum spanning tree. It means that as the algorithm running, the number of trees in the forest decreases.
![img](https://raw.github.com/yankuangshi/algorithms-training/master/Kruskal/img/screenshot3.png)

## Pseudo Code

```
Step 1: Make an empty set for the final minimum spanning tree (MST)
Step 2: Make a set for each vertex of G, where each set is a single node tree
Step 3: Sort the edges of G in ascending order
Step 4: For each edge (vertex1, vertex2) in the sorted edges of step 3:
			If vertex1 and vertex2 belong to different set:
				Add the edge (vertex1, vertex2) to MST
				Get together vertex1 and vertex2 in one single tree
Step 5: Return MST
```

## Final result of the example
![img](https://raw.github.com/yankuangshi/algorithms-training/master/Kruskal/img/screenshot5.png)
![img](https://raw.github.com/yankuangshi/algorithms-training/master/Kruskal/img/screenshot4.png)
