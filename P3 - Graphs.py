#!/usr/bin/python3
import random
random.seed()

class Graph():
    def __init__ (self):
        self.adjList = {}

    def addNode (self, nodeVal):
        # Using a set for constant lookup time, less memory.
        self.adjList[nodeVal] = set()

    def addUndirectedEdge(self, first, second):
        self.adjList[first].add(second)
        self.adjList[second].add(first)

    def removeUndirectedEdge(self, first, second):
        if second in self.adjList[first]:
            self.adjList[first].remove(second)
            self.adjList[second].remove(first)

    def getAllNodes(self):
        return self.adjList

class GraphSearch:
    def DFSRec(self, start, end, graph):
        visited = []
        nodeStack = [start]
        self._DFSRec(start, end, visited, nodeStack, graph)

        if (visited[-1] is end):
            return visited
        else:
            return None
    
    def _DFSRec(self, start, end, visited, nodeStack, graph):
        if (nodeStack):
            currNode = nodeStack.pop()
        else:
            return
        visited.append(currNode)

        if (currNode is end):
            return
        
        for neighbor in graph.adjList[currNode]:
            if neighbor not in visited:
                nodeStack.append(neighbor)
        
        self._DFSRec(start, end, visited, nodeStack, graph)
            
    def DFSIter(self, start, end, graph):
        visited = []
        nodeStack = [start]

        while nodeStack:
            currNode = nodeStack.pop()
            visited.append(currNode)

            if currNode is end:
                return visited

            for neighbor in graph.adjList[currNode]:
                if neighbor not in visited:
                    nodeStack.append(neighbor)

        return None

    def BFTRec(self, graph):
        # Convert all the dictionary keys into a list
        unvisitedNodes = [*graph.adjList]
        visited = []

        self._BFTRec(unvisitedNodes, visited, [unvisitedNodes[0]], graph)
        return visited
    
    def _BFTRec(self, unvisitedNodes, visited, nodeQueue, graph):
        if (len(unvisitedNodes) is 0):
            return visited
        
        currNode = nodeQueue.pop(0)
        visited.append(currNode)
        unvisitedNodes.remove(currNode)

        for neighbor in graph.adjList[currNode]:
            if neighbor not in visited and neighbor in unvisitedNodes and neighbor not in nodeQueue:
                nodeQueue.append(neighbor)

        if (len(nodeQueue) is 0 and len(unvisitedNodes) is not 0):
            nodeQueue.append(unvisitedNodes[0])
        
        return (self._BFTRec(unvisitedNodes, visited, nodeQueue, graph))

    def BFTIter(self, graph):
        # Convert the dictionary keys into a list.
        unvisitedNodes = [*graph.adjList]
        visited = []
        nodeQueue = [unvisitedNodes[0]]

        while (nodeQueue):
            currNode = nodeQueue.pop(0)
            visited.append(currNode)
            unvisitedNodes.remove(currNode)

            for neighbor in graph.adjList[currNode]:
                if neighbor not in visited and neighbor in unvisitedNodes and neighbor not in nodeQueue:
                        nodeQueue.append(neighbor)
            
            if (len(nodeQueue) is 0 and len(unvisitedNodes) is not 0):
                nodeQueue.append(unvisitedNodes[0])

        return visited

def createLinkedList(n):
    # Create nodes up to n, add edges between adjacent nodes
    linkedGraph = Graph()
    for i in range(n):
        linkedGraph.addNode(i)
    
    for i in range(n-1):
        linkedGraph.addUndirectedEdge(i, i+1)
    
    return linkedGraph

def createRandomUnweightedGraphIter(n):
    randGraph = Graph()
    # Generate nodes 0-(n-1) and add them to the graph
    for i in range(n):
        randGraph.addNode(i)
    
    # Generate two random numbers up to n, create an edge between them.
    for i in range(n):
        randGraph.addUndirectedEdge(random.randint(0, n-1), random.randint(0, n-1))
    return randGraph

def BFTRecLinkedList(graph):
    print(GraphSearch.BFTRec(graph))

def BFTIterLinkedList(graph):
    print(GraphSearch.BFTIter(graph, graph))

randomGraph = createRandomUnweightedGraphIter(40)

randomGraphDict = randomGraph.getAllNodes()
for key in randomGraphDict:
    print(f"{key} : {randomGraphDict[key]}")

print("")
print("Recursive DFS:\n"+str(GraphSearch().DFSRec(2, 20, randomGraph))+"\n")
print("Iterative DFS:\n"+str(GraphSearch().DFSIter(2, 20, randomGraph))+"\n")

print("Recursive BFT:\n"+str(GraphSearch().BFTRec(randomGraph))+"\n")
print("Iterative BFT:\n"+str(GraphSearch().BFTIter(randomGraph))+"\n")

linkedGraph = createLinkedList(40)
BFTIterLinkedList(linkedGraph)