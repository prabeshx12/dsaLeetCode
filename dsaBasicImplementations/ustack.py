# Implementation of Stack in python
class Stack:
    def __init__(self, length):
        self.stk = [None] * length
        self.top = -1

    def push(self, val):
        if self.top == len(self.stk) - 1:
            print("Error: Stack is full")
            return
        self.top += 1
        self.stk[self.top] = val
        
    def pop(self):
        if self.top == -1:
            print("Error: Can't pop from the empty stack")
            return None

        value = self.stk[self.top]
        self.stk[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            print("Error: Stack is empty")
            return None
        return self.stk[self.top]
        

stack1 = Stack(4)

list1 = [1, 2, 4, 3]

for num in list1:
    stack1.push(num)

for i in range(3):
    print(stack1.pop())

print(stack1.peek())
