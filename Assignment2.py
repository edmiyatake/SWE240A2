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

#TASK 2 TEST CASES