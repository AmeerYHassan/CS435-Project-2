#!/usr/bin/python3
import random
import collections

class DirectedGraph:
    def __init__(self):
        # Directed graph with an adjacency list.
        self.graphNodes = {}
    
    def addNode(self, nodeVal):
        if nodeVal not in self.graphNodes:
            self.graphNodes[nodeVal] = set()
    
    def addDirectedEdge(self, first, second):
        if first in self.graphNodes:
            self.graphNodes[first].add(second)
    
    def removeDirectedEdge(self, first, second):
        if second in self.graphNodes[first]:
            self.graphNodes[first].remove(second)
    
    def getAllNodes(self):
        return self.graphNodes
    
    def getNeighbors(self, node):
        return self.graphNodes[node]

class TopSort:
    @staticmethod
    def Kahns(self, graph):
        dependencyDict = genDependencyDict(graph)
        finalOutput = []
        dependencyQueue = collections.deque()

        updateDependencyDict(dependencyDict, dependencyQueue)
        
        while(dependencyQueue):
            currNode = dependencyQueue[0]
            finalOutput.append(currNode)

            for neighbor in graph.graphNodes:
                dependencyDict[neighbor] -= 1

            updateDependencyDict(dependencyDict, dependencyQueue)
            dependencyQueue.popleft()

        return finalOutput

    def mDFS(self, graph):
        nodeStack = []
        visitedDict = {}
        
        for node in list(graph.graphNodes):
            visitedDict[node] = False
        
        for node in list(graph.graphNodes):
            if (not visitedDict[node]):
                self.mDFS_Helper(node, nodeStack, visitedDict, graph)

        return nodeStack
        
    def mDFS_Helper(self, currNode, stack, visitedDict, graph):
        visitedDict[currNode] = True
        for neighbor in graph.graphNodes[currNode]:
            if (not visitedDict[neighbor]):
                self.mDFS_Helper(neighbor, stack, visitedDict, graph)
        stack.insert(0, currNode)

def updateDependencyDict(dependencyDict, dependencyQueue):
    for node in list(dependencyDict):
        if dependencyDict[node] == 0:
            dependencyQueue.append(node)
            dependencyDict[node] = -1

def genDependencyDict(graph):
    nodeList = [*graph.graphNodes]
    dependencyDict = {}

    for node in nodeList:
        dependencyDict[node] = 0
    
    for node in nodeList:
        for neighbor in graph.getNeighbors(node):
            dependencyDict[neighbor]+=1
    
    return dependencyDict
    
def createRandomDAGIter(n):
    randomDag = DirectedGraph()
    for i in range(n):
        randomDag.graphNodes[i] = set()
    
    for i in range(n):
        # Generate up to 8 random edges for a node
        for j in range(random.randint(1, 8)):
            if (i+1 == n-1 or i+1 > n-1):
                continue
            else:
                randomDag.addDirectedEdge(i, random.randint(i+1, n-1))
    return randomDag

randomGraph = createRandomDAGIter(100)
print(TopSort().mDFS(randomGraph))

directedG = DirectedGraph()
directedG.addNode(1)
directedG.addNode(2)
directedG.addNode(3)
directedG.addNode(4)
print(directedG.getAllNodes())
directedG.addDirectedEdge(1, 2)
directedG.addDirectedEdge(1, 3)
directedG.addDirectedEdge(2, 4)
print(directedG.getAllNodes())
directedG.removeDirectedEdge(1, 2)
directedG.removeDirectedEdge(2, 4)
print(directedG.getAllNodes())
