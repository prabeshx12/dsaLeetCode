class uCircQueue:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size of the queue must be a positive integer")
        
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        
        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.queue[self.front]

        if self.front == self.rear:
            # Queue has only one element, reset to empty state
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        index = self.front

        while True:
            print(self.queue[index], end=" ")

            if index == self.rear:
                break

            index = (index + 1) % self.size
        print()


queue = uCircQueue(5)
# Enqueue elements
for i in range(1, 6):
    queue.enqueue(i)

print("Queue after enqueuing:")
queue.display() 

# Dequeue two elements
print("Dequeued elements:")
for _ in range(2):
    print(queue.dequeue())

print("Queue after dequeuing:")
queue.display()
