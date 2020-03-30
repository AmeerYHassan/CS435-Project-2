# CS435 Project 2
## Exploring graphs and graph-searching functions

This project's purpose is to explore the functionality of graphs, implementing graphs, and implementing various different searching algorithms for graphs.

### Part One:
Part one had us implement various different functions, including an implementation of a graph class as well as various different searching and traversal algorithms.

* Graph Class
  * The graph class uses an adjacency list to represent the graph. The adjacency list itself is a dictionary, with the value to the key being a set of connected nodes.
  * `def addNode(nodeVal)` - Adds a node to the graph.
  * `def addUndirectedEdge(first, second)` - Adds an undirected edge between two nodes.
  * `def removeUndirectedEdge(first, second)` - Removes an undirected edge between two nodes.
  * `def getAllNodes()` - Returns the adjacency list used as the graph representation.
  * `def createRandomUnweightedGraph(n)` - Generates a random graph with n nodes and n random edges.
  * `def createLinkedList(n)` - Creates a linked list with graphs, each adjacent node has an edge between them

* Searching Algorithms
  * `DFSRec(start, end)` - A recursive implementation of Depth-First Search. Returns a valid depth first search from the `start` node to the `end` node.
  * `DFSIter(start, end)` - Similar to `DFSRec`, but implemented iteratively.
  * `BFTRec()` - A breadth first traversal function implemented recursively. Returns a valid breadth first traversal.
  * `BFTIter()` - Similar to `BFTRec()`, but implemented iteratively.

#### Test-Cases for Part One:
```python
randomGraph = Graph()
randomGraph.createRandomUnweightedGraphIter(40)

randomGraphDict = randomGraph.getAllNodes()
for key in randomGraphDict:
    print(f"{key} : {randomGraphDict[key]}")

print("")
print("Recursive DFS:\n"+str(randomGraph.DFSRec(2, 20))+"\n")
print("Iterative DFS:\n"+str(randomGraph.DFSIter(2, 20))+"\n")

print("Recursive BFT:\n"+str(randomGraph.BFTRec())+"\n")
print("Recursive BFT:\n"+str(randomGraph.BFTIter())+"\n")
```

Output:
```
0 : {11, 20}
1 : {18, 20}
2 : {24, 26, 38}
3 : {33, 11}
4 : {33}
5 : {39}
6 : {17, 13}
7 : set()
8 : {14}
9 : {39, 15}
10 : {10, 28, 30}
11 : {0, 3, 30}
12 : set()
13 : {32, 6}
14 : {8, 29}
15 : {9, 22, 30}
16 : set()
17 : {6}
18 : {1, 26, 27}
19 : {33}
20 : {0, 1, 27}
21 : {28}
22 : {33, 35, 15}
23 : {36}
24 : {2, 29, 39}
25 : {32}
26 : {18, 2}
27 : {18, 20}
28 : {10, 21}
29 : {24, 14}
30 : {10, 11, 15}
31 : {34}
32 : {25, 35, 13}
33 : {3, 19, 4, 22}
34 : {31}
35 : {32, 22}
36 : {23}
37 : set()
38 : {2}
39 : {24, 9, 5, 39}

Recursive DFS:
[2, 38, 26, 18, 27, 20]

Iterative DFS:
[2, 38, 26, 18, 27, 20]

Recursive BFT:
[0, 11, 20, 3, 30, 1, 27, 33, 10, 15, 18, 19, 4, 22, 28, 9, 26, 35, 21, 39, 2, 32, 24, 5, 38, 25, 13, 29, 6, 14, 17, 8, 7, 12, 16, 23, 36, 31, 34, 37]

Recursive BFT:
[0, 11, 20, 3, 30, 1, 27, 33, 10, 15, 18, 19, 4, 22, 28, 9, 26, 35, 21, 39, 2, 32, 24, 5, 38, 25, 13, 29, 6, 14, 17, 8, 7, 12, 16, 23, 36, 31, 34, 37]
```

