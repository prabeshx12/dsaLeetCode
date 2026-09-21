# Implementation of Linear Queue in python
class Queue:
    def __init__(self, length):
        self.lst = [None] * length
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return self.rear == len(self.lst) - 1

    def peek(self):
        if self.isEmpty():
            print("Error: queue is empty.")
            return None

        return self.lst[self.front + 1]

    def enqueue(self, val):
        if self.isFull():
            print("Error: can't enqueue, queue is full.")
            return

        self.rear += 1
        self.lst[self.rear] = val

    def dequeue(self):
        if self.isEmpty():
            print("Error: can't dequeue, queue is empty.")
            return None

        self.front += 1
        value = self.lst[self.front]
        self.lst[self.front] = None
        return value

