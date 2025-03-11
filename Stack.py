class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity  # Fixed-size array (C-style array)
        self.top = -1  # -1 indicates the stack is empty
        self._size = 0  # Track the size of the stack

    def push(self, value):
        if self._size == self.capacity:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value
            self._size += 1  # Increment the size

    def pop(self):
        if self._size == 0:
            print("Stack Underflow")
            return None
        else:
            value = self.stack[self.top]
            self.top -= 1
            self._size -= 1  # Decrement the size
            return value

    def peek(self):
        if self._size == 0:
            print("Stack is empty")
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self._size == 0

    def get_size(self):  # Return the size of the stack
        return self._size

    def __str__(self):
        # Return a string representation of the stack
        if self._size == 0:
            return "Stack is empty"
        return " -> ".join(str(self.stack[i]) for i in range(self._size))

# Example usage
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack contents:", stack)
stack.pop()
print("Stack  after pop contents:", stack)
stack.peek()
print("top element using peek :", stack.peek())
print("Is stack empty:", stack.is_empty())  # False
print("Size of stack:", stack.get_size())  # 2
