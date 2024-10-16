class Stack:
    def __init__(self):
        self.data = []
    
    def isEmpty(self):
        return len(self.data) == 0
    
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
    
def equationSolver(eq):
        # Goal is to split the numbers from the operators
        numbers = Stack()
        operators = Stack()
        equation = eq.split()

        for term in equation:
            if term.isdigit():
                numbers.push(term)
            elif term == "+" or term == "-" or term == "*" or term == "/":
                operators.push(term)
            else:
                # anything needs to return Nan or None
                print("Nan => STRING IN EQUATION")
                return None

        while not operators.isEmpty():
            numerand1 = int(numbers.pop())
            numerand2 = int(numbers.pop())
            if operators.size() > 0:
                op = operators.pop()
            else:
                break
            if op == "+":
                numbers.push(numerand2 + numerand1)
                continue
            elif op == "-":
                numbers.push(numerand2 - numerand1)
                continue
            if op == "*":
                numbers.push(numerand2 * numerand1)
                continue
            elif op == "/":
                numbers.push(numerand2 / numerand1)
                continue
            else:
                break

        return numbers.printStack()

# the viable way I see that task 2 has to work
# a fucntion that takes in an equation and returns the solution
# problem:
# 1. I can put numbers and operands into different stacks but I need to know the order in which I apply them
# helper function?

    

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
eq1 = "10 + 20 * 2"
eq2 = "foo / 30 + 7"
eq3 = "10 + 20 - 47 * 2"
eq4 = "28 / 4"
equationSolver(eq1)
equationSolver(eq2)
equationSolver(eq3)
equationSolver(eq4)