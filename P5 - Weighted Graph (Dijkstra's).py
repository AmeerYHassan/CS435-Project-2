

import random
import math

class Node:
    def __init__(self, nodeVal):
        self.nodeVal = nodeVal
        self.neighbors = {}
    
    def __repr__(self):
        return str(self.neighbors)

class WeightedGraph:
    def __init__(self):
        self.graphNodes = {}
    
    def addNode(self, nodeVal):
        self.graphNodes[nodeVal] = Node(nodeVal)
    
    def addWeightedEdge(self, first, second, edgeWeight):
        self.graphNodes[first].neighbors[second] = edgeWeight
    
    def removeDirectedEdge(self, first, second):
        self.graphNodes[first].neighbors.pop(second)
    
    def findNode(self, nodeVal):
        return self.graphNodes[nodeVal]

    def getAllNodes(self):
        return self.graphNodes

def createRandomCompleteWeightedGraph(n):
    randGraph = WeightedGraph()

    for i in range(n):
        randGraph.addNode(i)
    
    nodeList = [*randGraph.graphNodes]
    for firstNode in nodeList:
        for secondNode in nodeList:
            if (firstNode is not secondNode):
                randGraph.addWeightedEdge(firstNode, secondNode, random.randint(1, max(10, n/2)))
    
    return randGraph

def createLinkedList(n):
    linkedGraph = WeightedGraph()

    for i in range(n):
        linkedGraph.addNode(i)
    
    for i in range(n-1):
        linkedGraph.addWeightedEdge(i, i+1, 1)
    
    return linkedGraph

# NOTE: Graph only used to find neighbors of a node.
def dijkstras(start, graph):
    currNode = graph.findNode(start)
    currVal = start

    distanceDict = {}
    distanceDict[currVal] = 0

    visitedNodes = set()
    # While curr is not null and currVal is in the dictionary
    while(currVal is not None and currVal in distanceDict):
        # “Finalize” curr.
        visitedNodes.add(currVal)

        # Iterate over its neighbors, “relax” each neighbor:
        for neighbor in [*currNode.neighbors]:
            # Not finalized Neighbor
            if (neighbor not in visitedNodes):
                updatedDistance = distanceDict[currVal] + currNode.neighbors[neighbor]
                if (neighbor not in distanceDict or updatedDistance < distanceDict[neighbor]):
                    distanceDict[neighbor] = updatedDistance
        currVal = minDist(distanceDict, visitedNodes)
        if (currVal is not None):
            currNode = graph.findNode(currVal)
        else:
            break

    return distanceDict

# Returns the node with smallest distance (Taken from repl.it)
def minDist(distanceDict, visitedNodes):
    ans = None
    m = math.inf
    for curr in [*distanceDict]:
        if curr not in visitedNodes and distanceDict[curr] <= m:
            m = distanceDict[curr]
            ans = curr
    return ans