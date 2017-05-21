class Node:

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None
        
class AVL_tree:

    def __init__(self):
        self.root = None

    def calcHeight(self, node):
        if not node:
            return -1

        return node.height

    def height_tree(self):
        return max(self.calcHeight(self.root), self.calcHeight(self.root)) + 1

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)
        
        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)

        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)

        else:
            if not node.leftChild and not node.rightChild:
                print("removing a leaf node")
                del node
                return None
            
            if not node.leftChild:
                print("removing a node with only right Child")
                tempNode = node.rightChild
                del node
                return tempNode
            
            elif not node.rightChild:
                print("removing a node with only left Child")
                tempNode = node.leftChild
                del node
                return tempNode

            print("removing a node with both children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcbalance(node)

        if balance > 1 and self.calcbalance(node.leftChild) >= 0:
            return rotateright(node)

        if balance > 1 and self.calcbalance(node.leftChild) < 0:
            node.leftChild = self.rotateleft(node.leftChild)
            return self.rotateright(node)

        if balance < -1 and self.calcbalance(node.rightChild) > 0:
            node.rightChild = self.rotateright(node.leftChild)
            return self.rotateleft(node)

        if balance < -1 and self.calcbalance(node.rightChild) <= 0:
            return self.rotateleft(node)

        return node
  
    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node
    
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print(node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def settleViolation(self, data, node):

        balance = self.calcbalance(node)

        if balance > 1 and data < node.leftChild.data:
            print("Doubly left heavy")
            return self.rotateright(node)

        elif balance < -1 and data > node.rightChild.data:
            print("Doubly right heavy")
            return self.rotateleft(node)

        elif balance > 1 and data > node.leftChild.data:
            print("left right rotation")
            node.leftChild = self.rotateleft(node.leftChild)
            return self.rotateright(node)
        
        elif balance < -1 and data < node.rightChild.data:
            print("right left rotation")
            node.rightChild = self.rotateright(node.rightChild)
            return self.rotateleft(node)

        return node
        
#If the return value of the below function is > 1 => the tree is left heavy and we need a right rotation
#                                      ... is < -1 => the tree is right heavy and we need a left rotation
    def calcbalance(self, node):
        if not node:
            return 0

        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rotateright(self, node):

        print("rotating the node {} right" .format(node.data))

        templeftChild = node.leftChild
        t = templeftChild.rightChild

        templeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        templeftChild.height = max(self.calcHeight(templeftChild.leftChild),self.calcHeight(templeftChild.rightChild)) + 1

        return templeftChild

    def rotateleft(self, node):

        print("rotating the node {} to left" .format(node.data))

        temprightChild = node.rightChild
        t = temprightChild.leftChild

        temprightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        temprightChild.height = max(self.calcHeight(temprightChild.leftChild),self.calcHeight(temprightChild.rightChild)) + 1

        return temprightChild
