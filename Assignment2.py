class Stack:
    def __init__(self):
        self.data = []
    
    def push(self,element):
        self.data.append(element)
 
    def pop(self):
        if not self.data:
            raise Exception("stack is empty")
        else:
            return self.data.pop()
    
    def peek(self):
        if not self.data:
            raise Exception("stack is empty")
        else:
            return self.data[-1]
    
    def size(self):
        return len(self.data)

    def printStack(self):
        for i in range(len(self.data)):
            print(self.data[i])
        return 0

# the viable way I see that task 2 has to work
# a fucntion that takes in an equation and returns the solution
# problem:
# 1. I can put numbers and operands into different stacks but I need to know the order in which I apply them
# helper function?

def order(command):
    if command == "*" or command ="/":
        return 10
    elif command == "+" or command == "-":
        return 1
    else:
        # invalid command
        return -1

    

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
