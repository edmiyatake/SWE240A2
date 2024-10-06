class Stack:
    def __init__(self):
        self.data = []
    
    def push(self,element):
        self.data.append(element)
 
    def pop(self):
        self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def size(self):
        return len(self.data)

    def printStack(self):
        for i in range(len(self.data)):
            print(self.data[i])
        return 0

def calculator(str):
    newStack = Stack()
    for char in str:
        newStack.push(char)
    newStack.printStack()
    return -1

    

class Queue:
    def __init__(self):
        self.front = 0
        self.data = []
    
    def enqueue(self,element):
        self.data.append(element)
    
    def dequeue(self):
        if self.size() == 0:
            raise Exception("Queue is empty")
        else:   
            solution = self.data[self.front]
            self.data[self.front] = None
            self.front += 1
            return solution
            
    
    def poll(self):
        return self.data[self.front]
    
    def size(self):
        return len(self.data) - self.front

class stackWithTwoQs:
    def __init__(self):
        self.queueOne = Queue()
        self.queueTwo = Queue()
    
    def push(self,x):
        exit

    def pop(self):
        exit
    
    def peek(self):
        exit
    
    def size(self):
        exit

# TASK 1 TEST CASES
# newStack = Stack()
# newStack.push(32)
# print(newStack.peek())
# print(newStack.size())
# newStack.push(46)
# print(newStack.peek())
# newStack.push(97)
# print(newStack.peek())
# print(newStack.size())
# newStack.pop()
# print(newStack.peek())
# print(newStack.size())

# TASK 2 TEST CASES

# TASK 3 TEST CASES 
# newQueue = Queue()
# newQueue.dequeue()
# newQueue.enqueue(36)
# print(newQueue.size())
# newQueue.enqueue(23)
# print(newQueue.size())
# newQueue.enqueue(33)
# print(newQueue.size())
# newQueue.enqueue(900)
# print(newQueue.size())
# print(newQueue.dequeue())
# print(newQueue.poll())

# TASK 4 TEST CASES
print(calculator("50 + 67 * 42"))