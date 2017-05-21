class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

class Queue:

    def __init__(self):
        self.head = None
        self.size = 0

    def IsEmpty(self):
        return self.head == None
    
    def enqueue(self, data):
        currentnode = None
        
        newnode = Node(data)

        if self.head is not None:
            currentnode = self.head
        else:
            self.head = newnode
            currentnode = self.head
        
        while currentnode.nextnode is not None:
            currentnode = currentnode.nextnode
        currentnode.nextnode = newnode
        newnode.nextnode = None
    
    def dequeue(self):
        currentnode = self.head
        self.head = currentnode.nextnode
        return currentnode.data

    def peek(self):
        return self.head.data

    def print_queue(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.data)
            currentnode = currentnode.nextnode 

    def size_queue(self):
        self.size = 0
        currentnode = self.head
        while currentnode is not None:
            self.size += 1
            currentnode = currentnode.nextnode
        return self.size

