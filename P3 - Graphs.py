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
        self.adjList[first].remove(second)
        self.adjList[second].remove(first)

    def getAllNodes(self):
        return self.adjList

    def createRandomUnweightedGraphIter(self, n):
        # Generate nodes 0-(n-1) and add them to the graph
        for i in range(n):
            self.addNode(i)
        
        # Generate two random numbers up to n, create an edge between them.
        for i in range(n):
            self.addUndirectedEdge(random.randint(0, n-1), random.randint(0, n-1))

    def createLinkedList(self, n):
        # Create nodes up to n, add edges between adjacent nodes
        for i in range(n):
            self.addNode(i)
        
        for i in range(n-1):
            self.addUndirectedEdge(i, i+1)
    
    def DFSRec(self, start, end):
        # Recursive DFS, implemented with a stack.
        visited = []
        nodeStack = [start]
        self._DFSRec(start, end, visited, nodeStack)

        # If the last node in the DFS is the end node, print out the visited order.
        if (visited[-1] is end):
            return visited
        else:
            return None
    
    def _DFSRec(self, start, end, visited, nodeStack):
        if (nodeStack):
            currNode = nodeStack.pop()
        else:
            return
        visited.append(currNode)

        # If we have found the target, return.
        if (currNode is end):
            return
        
        # Add all of the neighbors to the stack.
        for neighbor in self.adjList[currNode]:
            if neighbor not in visited:
                nodeStack.append(neighbor)
        
        self._DFSRec(start, end, visited, nodeStack)
            
    def DFSIter(self, start, end):
        visited = []
        nodeStack = [start]

        while nodeStack:
            currNode = nodeStack.pop()
            visited.append(currNode)

            if currNode is end:
                return visited

            for neighbor in self.adjList[currNode]:
                if neighbor not in visited:
                    nodeStack.append(neighbor)

        return None

    def BFTRec(self):
        # Convert all the dictionary keys into a list
        unvisitedNodes = [*self.adjList]
        visited = []

        # Call the helper function
        self._BFTRec(unvisitedNodes, visited, [unvisitedNodes[0]])
        return visited
    
    # Helper function
    def _BFTRec(self, unvisitedNodes, visited, nodeQueue):
        if (len(unvisitedNodes) is 0):
            return visited
        
        currNode = nodeQueue.pop(0)
        visited.append(currNode)
        unvisitedNodes.remove(currNode)

        for neighbor in self.adjList[currNode]:
            if neighbor not in visited and neighbor in unvisitedNodes and neighbor not in nodeQueue:
                nodeQueue.append(neighbor)

        # If the queue is empty but there are still unvisitedNodes, add the first unvisited Node.
        if (len(nodeQueue) is 0 and len(unvisitedNodes) is not 0):
            nodeQueue.append(unvisitedNodes[0])
        
        return (self._BFTRec(unvisitedNodes, visited, nodeQueue))

    def BFTIter(self):
        # Convert the dictionary keys into a list.
        unvisitedNodes = [*self.adjList]
        visited = []
        nodeQueue = [unvisitedNodes[0]]

        # While the queue is not empty...
        while (nodeQueue):
            currNode = nodeQueue.pop(0)
            visited.append(currNode)
            unvisitedNodes.remove(currNode)

            for neighbor in self.adjList[currNode]:
                if neighbor not in visited and neighbor in unvisitedNodes and neighbor not in nodeQueue:
                        nodeQueue.append(neighbor)
            
            if (len(nodeQueue) is 0 and len(unvisitedNodes) is not 0):
                nodeQueue.append(unvisitedNodes[0])

        return visited

def BFTRecLinkedList(graph):
    print(graph.BFTRec())

def BFTIterLinkedList(graph):
    print(graph.BFTIter())

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
