#!/usr/bin/python3
import random

class GridNode:
    def __init__(self, nodeVal, xCoord, yCoord):
        self.nodeVal = nodeVal
        self.neighbors = set()
        self.coords = (xCoord, yCoord)
    
    def __repr__(self):
        return(str(self.neighbors))

class GridGraph:
    def __init__(self):
        self.nodeList = {}

    def addGridNode(self, x, y, nodeVal):
        self.nodeList[nodeVal] = GridNode(nodeVal, x, y)

    def addUndirectedEdge(self, first, second):
        self.nodeList[first].neighbors.add(second)
        self.nodeList[second].neighbors.add(first)

    def removeUndirectedEdge(self, first, second):
        self.nodeList[first].neighbors.remove(second)
        self.nodeList[second].neighbors.remove(first)

    def getAllNodes(self):
        return self.nodeList

def createRandomGridGraph(n):
    randomGrid = GridGraph()
    for i in range(n):
        for j in range(n):
            randomGrid.addGridNode(j, i, j+i*n)
    
    for i in range(n*n):
        currNeighbors = getNeighbors(randomGrid.nodeList[i], n)
        for neighbor in currNeighbors:
            if(random.randint(0, 1) is 0):
                randomGrid.addUndirectedEdge(i, neighbor)
    
    return randomGrid

def getNeighbors(node, n):
    if (node.coords[0] is 0):
        if (node.coords[1] is 0):
            return ([node.nodeVal+1, node.nodeVal+n])
        elif (node.coords[1] is n-1):
            return ([node.nodeVal+1, node.nodeVal-n])
        else:
            return ([node.nodeVal+1, node.nodeVal+n, node.nodeVal-n])
    elif (node.coords[0] is n-1):
        if (node.coords[1] is 0):
            return ([node.nodeVal-1, node.nodeVal+n])
        elif (node.coords[1] is n-1):
            return ([node.nodeVal-1, node.nodeVal-n])
        else:
            return ([node.nodeVal-1, node.nodeVal+n, node.nodeVal-n])
    elif (node.coords[1] is 0):
        return ([node.nodeVal-1, node.nodeVal+1, node.nodeVal+n])
    elif (node.coords[1] is n-1):
        return ([node.nodeVal-1, node.nodeVal+1, node.nodeVal-n])
    else:
        return([node.nodeVal-1, node.nodeVal+1, node.nodeVal+n, node.nodeVal-n])

def astar(sourceNode, destNode):
    # TODO: Implement astar
    pass

myGrid = createRandomGridGraph(5)
print(myGrid.getAllNodes())

