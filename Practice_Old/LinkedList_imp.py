#Linked List implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

class Linkedlist:
#initialize the class
    def __init__(self):
        self.head = None
        self.size = 0
#insert at the beginning
    def insertstart(self, data):
        self.size = self.size + 1

        newnode = Node(data)

        if not self.head:
            self.head = newnode
        else:
            newnode.nextnode = self.head
            self.head = newnode   
#insert at a given position
    def insert_position(self,data,index_pos):
        
        newnode = Node(data)
        currentnode = self.head
        previousnode = None
        position = 0
        self.size += 1
        if self.size1() < index_pos:
            return 'Invalid index. returning...'
        else:
            while position != index_pos:
                previousnode = currentnode
                currentnode = currentnode.nextnode
                position += 1
            previousnode.nextnode = newnode
            newnode.nextnode = currentnode
#insert at the end
    def insertend(self,data):
        self.size += 1

        newnode = Node(data)
        actualnode = self.head
        if not self.head:
            self.head = newnode
        else:
            while actualnode.nextnode is not None:
                actualnode = actualnode.nextnode
            actualnode.nextnode = newnode
            newnode.nextnode = None
#traverse and print a linkedlist
    def traverselist(self):
        actualnode = self.head

        while actualnode is not None:
            print(actualnode.data)
            actualnode = actualnode.nextnode
#remove head
    def removestart(self):
        actualnode = self.head
        self.head = actualnode.nextnode
#remove a node
    def remove(self, data):
        currentnode = self.head
        previousnode = None

        self.size = self.size - 1

        if self.head is None:
            return

        while currentnode.data != data:
            previousnode = currentnode
            currentnode = currentnode.nextnode
            
        if previousnode is None:
            self.head = currentnode.nextnode
        else:
            previousnode.nextnode = currentnode.nextnode
#remove at the end
    def removeend(self):
        currentnode = self.head
        previousnode= None

        if self.head is None:
            return
        elif currentnode.nextnode is None:
            self.remove(currentnode)

        while currentnode.nextnode is not None:
            previousnode = currentnode
            currentnode = currentnode.nextnode
        
        previousnode.nextnode = None
#return size
    def size1(self):
        return self.size
#return size by reading the size of the linkedlist
    def size2(self):
        actualnode = self.head
        size = 0
        while actualnode is not None:
            size += 1
            actualnode = actualnode.nextnode
            
        return size  
    
