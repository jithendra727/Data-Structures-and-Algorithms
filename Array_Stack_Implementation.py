class ArrayStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack_array = [None] * max_size
        self.top = -1

    def push(self, data):
        if self.is_full():
            raise RuntimeError("Stack is Full")
        self.top += 1
        self.stack_array[self.top] = data

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is Empty")
        data = self.stack_array[self.top]
        self.stack_array[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Stack is Empty")
        return self.stack_array[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1


# Example usage:
stack = ArrayStack(5)

stack.push(10)
stack.push(16)
stack.push(50)
stack.push(40)
stack.push(35)

print(stack.is_full())  # Output: True
print(stack.is_empty())  # Output: False
print(stack.peek())  # Output: 35
