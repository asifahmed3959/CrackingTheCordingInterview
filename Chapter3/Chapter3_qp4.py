from Chapter3.Stack import Stack




# First in First out


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, value):
        self.stack1.push(value)
        print("Successfully inserted a value")

    def pop(self):
        if self.stack1.size():
            self.copy()
        return self.stack2.pop()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()


    def peek(self):
        return self.stack2.peek()

    def copy(self):
        while self.stack1:
            self.stack2.push(self.stack1.pop())

        print("Successfully copied")