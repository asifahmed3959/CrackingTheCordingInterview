class Stack:
    def __init__(self):
        self.s = []

    def push(self, value):
        self.s.append(value)

    def pop(self):
        if self.is_empty():
            return float('inf')

        return self.s.pop()

    def peek(self):
        if self.is_empty():
            return float('inf')

        return self.s[-1]

    def size(self):
        return len(self.s)

    def is_empty(self):
        return len(self.s) == 0
