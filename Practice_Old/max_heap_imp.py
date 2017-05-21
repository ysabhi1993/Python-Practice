class Heap:
    HEAP_SIZE = 10
    def __init__(self):
        self.heap = [0] * HEAP_SIZE
        self.currentPosition = -1

    def insert(self, data):
        if self.isfull:
            return 'the heap is full'

        self.currentPosition += 1
        self.heap[self.currentPosition] = data
        self.fixUp(self.currentPosition)

    def fixUp(self, index):

        parentIndex = int((index - 1)/2)

        while parentIndex > 0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            index = parentIndex
            parentIndex = int((index - 1)/2)
        return

    def fixDown(self, index, upto):

        while index <= upto:
            leftChild = 2 * index + 1
            rightChild = 2 * index + 2

            if leftChild <= upto:           #checking with the least index(left child has the least) on a level. It also implies that 
                childToSwap = None          #node belonging to index 'upto' is from a level below the level of 'leftChild'.If this is violated => heap property is
                                            #in check
                if rightChild > upto:                   #If this is true - the 'upto' index has to come before rightChild
                    childToSwap = leftChild             #so swap with leftChild 
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break

                index = childToSwap
            else:
                break
                

    def isFull(self):
        if self.currentPosition == HEAP_SIZE:
            return True
        else:
            return False

    def heapsort(self):
        for i in range(0,self.currentPosition + 1):                 #currentPosition will be the last index
            temp = self.heap[self.currentPosition - i]              #swap the first and last elements
            print(temp)
            self.heap[self.currentPosition - i] = self.heap[0]
            self.heap[0] = temp
            self.fixDown(0,self.currentPosition - i - 1)            #the 'i' nodes are the once that are already considered for sorting
