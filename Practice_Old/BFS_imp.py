class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacencyList = []

class BreadthFirstSearch:

    def __init__(self, startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:

            actualNode = queue.pop(0)
            print(actualNode.name)

            for i in actualNode.adjacencyList:
                if not i.visited:
                    i.visited = True
                    queue.append(i)

#implement adjacencyList(self, node) function to return a list with all the adjacent nodes.
    
