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

    def traverse(self):
        if self.isEmpty():
            print("Error: can't traverse, queue is empty.")
            return

        for i in range(self.front + 1, self.rear + 1):
            print(self.lst[i], end = " ")


queue1 = Queue(4)
list1 = [10, 20, 30, 40]

print("Display of the queue after enqueuing")
for num in list1:
    queue1.enqueue(num)

queue1.traverse()

print("\nDequeued elements")
for _ in range(2):
    print(queue1.dequeue())

print("Queue after dequeue")
queue1.traverse()

print("\nLooking at the front of queue")
print(queue1.peek())
