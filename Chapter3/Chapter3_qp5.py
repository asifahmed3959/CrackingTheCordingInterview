import unittest

from Chapter3.Stack import Stack


class SortedStack():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, value):
        if self.s1.is_empty():
            self.s1.push(value) # 1
        else:
            self.insert_right_order(value)


    def insert_right_order(self, value):
        while not self.s1.is_empty() and self.s1.peek() < value:
            curr_pop = self.s1.pop()
            self.s2.push(curr_pop) # s2 -> 1


        self.s1.push(value) # 2

        while not self.s2.is_empty():
            self.s1.push(self.s2.pop()) # 2 1


    def peek(self):
        if self.is_empty():
            return None

        return self.s1[-1]

    def pop(self):
        if self.is_empty():
            return None

        return self.s1.pop()

    def is_empty(self):
        return self.s1.is_empty()

    def size(self):
        return self.s1.size()



class Tests(unittest.TestCase):
    def test_push_one(self):
        queue = SortedStack()
        queue.push(1)
        assert queue.size() == 1

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert queue.size() == 2
    #
    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.size() == 3

    def test_pop_one(self):
        queue = SortedStack()
        queue.push(1)
        assert queue.pop() == 1

    def test_pop_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert queue.pop() == 1
        assert queue.pop() == 2

    def test_pop_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3

    def test_push_mixed(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(1)
        queue.push(4)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4