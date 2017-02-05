class Node:
    def __init__(self, character):
        self.character = character
        self.leftNode = None
        self.rightNode = None
        self.middleNode = None
        self.value = 0

class TST:
    def __init__(self):
        self.rootNode = None

    def put(self, key, value):
        self.rootNode = self.putNode(self.rootNode, key, value, 0)

    def putNode(self, node, key, value, index):

        c = key[index]

        if node == None:
            node = Node(c)

        if c < node.character:
            node.leftNode = self.putNode(node.leftNode, key, value, index)

        elif c > node.character:
            node.rightNode = self.putNode(node.rightNode, key, value, index)

        elif index < len(key) - 1:
            node.middleNode = self.putNode(node.middleNode, key, value, index + 1)
        else:
            node.value = value

        return node

    def get(self, key):
        node = self.getNode(self.rootNode, key, 0)

        if node == None:
            return None

        return node.value

    def getNode(self, node, key, index):

        if node == None:
            return None

        c = key[index]

        if c < node.character:
            return self.getNode(node.leftNode, key, index)
        elif c > node.character:
            return self.getNode(node.rightNode, key, index)
        elif index < len(key) - 1:
            return self.getNode(node.middleNode, key, index + 1)
        else:
            return node
        
