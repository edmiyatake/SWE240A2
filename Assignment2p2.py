class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self,element):
        self.data.append(element)
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:   
            return self.data.pop(0)
            
    def poll(self):
        return self.data[0]
    
    def size(self):
        return len(self.data)

class stackWithTwoQs:
    def __init__(self):
        self.queueOne = Queue()
        self.queueTwo = Queue()
    
    def isEmpty(self):
        return self.queueOne.size() == 0
    
    def push(self,val):
        # Queues are first in first out and Stacks are last in first out
        # i think the best way to do this is to treat queueOne as the back and queueTwo as the front
        self.queueTwo.enqueue(val)

        while not self.queueOne.isEmpty():
            self.queueTwo.enqueue(self.queueOne.dequeue())
        
        self.queueOne,self.queueTwo = self.queueTwo, self.queueOne
        

    def pop(self):
        if self.queueOne.isEmpty():
            raise IndexError("Empty Stack")
        else:
            self.queueOne.dequeue()
        
    def peek(self):
        if self.queueOne:
            return self.queueOne.poll()
        return None
    
    def size(self):
        return self.queueOne.size()

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

# Task 4 Test Cases
newStack = stackWithTwoQs()
newStack.push(26)
newStack.push(46)
newStack.push(23)
newStack.push(656)
newStack.push(216)
print(newStack.peek())
print(newStack.size())