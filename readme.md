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