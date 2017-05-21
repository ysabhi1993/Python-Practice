class stack:

    def __init__(self):
        self.stack = []
        self.numOfItems = 0

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)
        self.numOfItems += 1

    def pop_stack(self):
        self.stack.remove(self.stack[-1])
        self.numOfItems -= 1

    def peek(self):
        return self.stack[-1]
    
    def size_stack(self):
        return self.numOfItems

    def print_stack(self):
        for i in self.stack:
            print(i)
            
    
