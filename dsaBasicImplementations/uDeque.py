class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def insert_front(self, value):
        if self.is_full():
            raise OverflowError("Deque is full")

        self.front = (self.front - 1) % self.capacity
        self.arr[self.front] = value
        self.size += 1

    def insert_rear(self, value):
        if self.is_full():
            raise OverflowError("Deque is full")

        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = value
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")

        value = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")

        rear = (self.front + self.size - 1) % self.capacity
        value = self.arr[rear]
        self.arr[rear] = None
        self.size -= 1
        return value

    def get_front(self):
        if self.is_empty():
            return None
        return self.arr[self.front]

    def get_rear(self):
        if self.is_empty():
            return None
        rear = (self.front + self.size - 1) % self.capacity
        return self.arr[rear]

    def display(self):
        return [
            self.arr[(self.front + i) % self.capacity]
            for i in range(self.size)
        ]


dq = Deque(5)

dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(5)

print(dq.display())

print(dq.delete_front())
print(dq.delete_rear()) 

print(dq.display()) 
