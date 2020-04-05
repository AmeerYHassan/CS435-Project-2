import random

class DirectedGraph:
    def __init__(self):
        # Directed graph with an adjacency list.
        self.graphNodes = {}
    
    def addNode(self, nodeVal):
        self.graphNodes[nodeVal] = set()
    
    def addDirectedEdge(self, first, second):
        self.graphNodes[first].add(second)
    
    def removeDirectedEdge(self, first, second):
        self.graphNodes[first].remove(second)
    
    def getAllNodes(self):
        return self.graphNodes

class TopSort:
    def Kahns(self, graph):
        dependencyDict = genDependencyDict(graph)
        finalOutput = []
        dependencyQueue = []

        updateDependencyDict(dependencyDict, dependencyQueue)
        
        while(dependencyQueue):
            currNode = dependencyQueue[0]
            finalOutput.append(currNode)

            for neighbor in graph.graphNodes:
                dependencyDict[neighbor] -= 1

            updateDependencyDict(dependencyDict, dependencyQueue)
            dependencyQueue.pop(0)

        return finalOutput

    def mDFS(self, graph):
        nodeStack = []
        visitedDict = {}
        
        for node in list(graph.graphNodes):
            visitedDict[node] = False
        
        for node in list(graph.graphNodes):
            if (not visitedDict[node]):
                self.mDFS_Helper(node, nodeStack, visitedDict, graph)

        nodeStack.reverse()
        return nodeStack

    def mDFS_Helper(self, currNode, stack, visitedDict, graph):
        visitedDict[currNode] = True
        for neighbor in graph.graphNodes[currNode]:
            if (not visitedDict[neighbor]):
                self.mDFS_Helper(neighbor, stack, visitedDict, graph)
        stack.append(currNode)

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
        for neighbor in graph.graphNodes[node]:
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
                randomDag.graphNodes[i].add(random.randint(i+1, n-1))
    return randomDag

currDAG = createRandomDAGIter(10)
topSortObj = TopSort()

print(topSortObj.Kahns(currDAG))
print(topSortObj.mDFS(currDAG))