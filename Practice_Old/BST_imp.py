class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

class Binary_ST:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertnode(data, self.root)
#if the tree is unbalanced, the insertion can take O(N) time instead of O(logN)
    def insertnode(self, data, node):
        if data < node.data:
            if node.left:
                self.insertnode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertnode(data, node.right)
            else:
                node.right = Node(data)
    
    def delete(self, data):
        if self.root:
            self.root = self.deleteNode(data, self.root)

    def deleteNode(self, data1, node):
        #if there is no such node, return it.
        if not node:
            return node
        #check if the data is smaller or larger than the root node and decide whether to go to the left of right.
        if data1 < node.data:
            node.left = self.deleteNode(data1, node.left)
        elif data1 > node.data:
            node.right = self.deleteNode(data1, node.right)
        else:
            #if the node we want to delete doesn't have either a left or a right child
            if not node.left and not node.right:
                print('removing a node with no children')
                del node
                return None
            # if the node has one of left or right child 
            if not node.left:
                tempnode = node.left
                print('removing a node with no left child')
                del node
                return tempnode
            elif not node.right:
                tempnode = node.right
                print('removing a node with no right child')
                del node
                return tempnode
            #if there are both children
            #first find the predecessor, which is the node having the greatest value on the left subtree.
            print('removing a node with both children')
            tempnode = self.getPredecessor(node.left)
            node.data = tempnode #swap the node (we want to delete) with the predecessor.
            node.left = self.deleteNode(tempnode.data, node.left)

        return node

    def getPredecessor(self, node):
        if node.right:
            getPredecessor(node.right)

        return node
      
    def minvalue(self):
        if self.root:
            return self.minvalueNode(self.root)

    def minvalueNode(self, node):
        if node.left:
            return self.minvalueNode(node.left)
        else:
            return node.data

    def maxvalue(self):
        if self.root:
            return self.maxvalueNode(self.root)

    def maxvalueNode(self, node):
        if node.right:
            return self.maxvalueNode(node.right)
        else:
            return node.data

    def traverse_BST(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self, node):
        if node.left:
            self.traverseInorder(node.left)
        print(node.data)
        if node.right:
            self.traverseInorder(node.right)
     
