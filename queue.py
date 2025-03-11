class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity  # Fixed-size array (C-style array)
        self.front = 0
        self.rear = -1
        self._size = 0  # Renaming the attribute to _size to avoid conflict

    def enqueue(self, value):
        if self._size == self.capacity:
            print("Queue Overflow")
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value
            self._size += 1

    def dequeue(self):
        if self._size == 0:
            print("Queue Underflow")
            return None
        else:
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self._size -= 1
            return value

    def peek(self):
        if self._size == 0:
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self._size == 0

    def get_size(self):  # Renamed method to avoid conflict with attribute
        return self._size


# Example usage
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(15)
print("Queue contents:", queue.queue)
print("top element using peek:",queue.peek()) #10
print("deque :",queue.dequeue()) # 10
print("queue  after dequeue:", queue.queue)
print("top element using peek:",queue.peek())  # 20
print("Is stack empty:", queue.is_empty())
print("Size of stack:", queue.get_size())
