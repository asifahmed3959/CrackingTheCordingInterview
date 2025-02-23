from Stack import Stack


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, value):
        super().push(value)

        if not self.min_stack or (self.min_stack and value <= self.min()):
            self.min_stack.push(value)

    def pop(self):
        if not super().is_empty():
            value_pop = super().pop()
            if value_pop == self.min_stack.peek():
                self.min_stack.pop()

            return value_pop

        return None

    def min(self):
        return self.min_stack.peek()


min_stack = MinStack()
min_stack.push(1)
min_stack.push(3)
min_stack.push(5)
min_stack.push(0)
min_stack.push(8)
min_stack.push(2)
print(min_stack.pop())
print(min_stack.min())
print(min_stack.pop())
print(min_stack.min())
print(min_stack.pop())
print(min_stack.min())

