# Dijkstra's algorithm

## Pseudocode

```
function Dijkstra(Graph, source):
	dist[source] := 0                     // Distance from source to source
	for each vertex v in Graph:			   // Initializations
    	if v ≠ source:
			dist[v] := infinity           // Unknown distance function from source to v
			previous[v] := undefined      // Previous node in optimal path from source
		end if 
		add v to Q                        // All nodes initially in Q
	end for
 
	while Q is not empty:                 // The main loop
		u := vertex in Q with min dist[u] // Source node in first case
		remove u from Q   

		for each neighbor v of u:         // where v has not yet been removed from Q.
			alt := dist[u] + length(u, v)
			if alt < dist[v]:             // A shorter path to v has been found
				dist[v]  := alt 
				previous[v]  := u 
			end if
		end for
	end while
	return dist[], previous[]
end function
```
(from [wikipedia](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm))

## Example

![img](https://raw.github.com/yankuangshi/algorithms-training/master/Dijkstra/dijkstra_example.png)

G is the source node.

|seq|nodes|A  |B  |C  |D  |E  |F  |H  |
|---|:---:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|G|∞|7,G|∞|∞|6,G|4,G|**3,G**|
|1|G,H|∞|6,H|∞|13,H|6,G|**4,G**|-|
|2|G,H,F|12,F|**6,H**|∞|13,H|6,G|-|-|
|3|G,H,F,B|10,B|-|16,B|13,H|**6,G**|-|-|
|4|G,H,F,B,E|**10,B**|-|16,B|12,E|-|-|-|
|5|G,H,F,B,E,A|-|-|16,B|**12,E**|-|-|-|
|6|G,H,F,B,E,A,D|-|-|**16,B**|-|-|-|-|
|7|G,H,F,B,E,A,D,C|-|-|-|-|-|-|-|

final distance table :

|d|A|B|C|D|E|F|G|H|
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|d|10|6|16|12|6|4|0|3|

final previous node table : 

|p|A|B|C|D|E|F|G|H|
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|p|B|H|B|E|G|G|G|G|

![img](https://raw.github.com/yankuangshi/algorithms-training/master/Dijkstra/dijkstra_result.png)



