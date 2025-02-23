import pytest


class MultiStack():
    def __init__(self):
        self.d = {}
        self.total_size = 9
        self.size = self.total_size // 3 # 333
        self.arr = [float('inf')] * self.total_size
        self.d[1] = (0, 2, 0) # start end curr
        self.d[2] = (3, 5, 3)  # start end curr
        self.d[3] = (6, 8, 6)  # start end curr

    def push(self, stack_number, value):
        if stack_number not in self.d:
            raise Exception(f'Stack Number : {stack_number} does not exist, please provide a proper stack value')

        start, end, curr = self.d[stack_number]

        if curr + 1 >= end:
            self.increase_size_and_copy()

        start, end, curr = self.d[stack_number]
        self.arr[curr] = value
        curr += 1
        self.d[stack_number] = (start, end, curr)
        print(f'Successfully inserted a value of {value} in stack_number: {stack_number}', "\n",
              f'Current Stack size {curr-start}')

    def increase_size_and_copy(self):
        new_total_size = self.total_size * 3 # 27
        new_arr = [float("inf")] * new_total_size # 27
        self.copy(new_arr, new_total_size)
        print(f'Successfully inserted the values, the current stands are {self.arr}', self.d)

    def copy(self, new_arr, new_total_size):
        new_each_size = new_total_size // 3 # 9
        copy_number = 1
        # Copy each stack
        for key in self.d.keys():
            start, end, curr = self.d[key] # 3, 5, 3

            new_start = (new_each_size * copy_number) - new_each_size # 0
            new_end = (new_each_size * copy_number) - 1 # 8

            j = new_start # 0
            for i in range(start, end+1, 1): # 0 to 2 ends at 3
                print(start, end+1, curr, i, self.arr)
                new_arr[j] = self.arr[i]
                j += 1

            new_curr = j # 3
            self.d[key] = (new_start, new_end, new_curr) # 0, 8, 3
            copy_number += 1

        self.arr = new_arr


    def pop(self, stack_number):
        if stack_number not in self.d:
            return -1

        start, end, curr = self.d[stack_number]

        if curr == start:
            return -1

        pop_value = self.arr[curr-1]
        self.arr[curr - 1] = float('inf')
        curr -= 1

        self.d[stack_number] = (start, end, curr)
        return pop_value


    def is_empty(self, stack_number):
        if stack_number not in self.d:
            return -1

        start, end, curr = self.d[stack_number]

        if curr == start:
            return True

        return False


    def peek(self, stack_number):
        if stack_number not in self.d:
            return -1

        start, end, curr = self.d[stack_number]
        if curr == start:
            return -1

        return self.arr[curr - 1]




# def test_multistack():
#     num_stacks = 3
#     stack_size = 6
#     s = MultiStack(stack_size=stack_size, number_of_stacks=num_stacks)
#
#     for stack_num in range(num_stacks):
#         assert s.is_empty(stack_num)
#         assert not s.is_full(stack_num)
#         with pytest.raises(StackEmptyError):
#             s.pop(stack_num)
#
#         for i in range(stack_size - 1):
#             s.push(i, stack_num=stack_num)
#             assert s.peek(stack_num) == i
#             assert not s.is_empty(stack_num)
#             assert not s.is_full(stack_num)
#
#         s.push(999, stack_num=stack_num)
#         with pytest.raises(StackFullError):
#             s.push(777, stack_num=stack_num)
#
#         assert not s.is_empty(stack_num)
#         assert s.is_full(stack_num)
#
#         assert s.peek(stack_num) == 999
#         assert s.pop(stack_num) == 999
#         assert not s.is_empty(stack_num)
#         assert not s.is_full(stack_num)
#
#         for i in range(stack_size - 2, 0, -1):
#             assert s.peek(stack_num) == i
#             assert s.pop(stack_num) == i
#             assert not s.is_empty(stack_num)
#             assert not s.is_full(stack_num)
#
#         assert s.peek(stack_num) == 0
#         assert s.pop(stack_num) == 0
#         assert s.is_empty(stack_num)
#         assert not s.is_full(stack_num)
#
#         with pytest.raises(StackEmptyError):
#             s.peek(stack_num)
#         with pytest.raises(StackEmptyError):
#             s.pop(stack_num)
#

# def test_stack_does_not_exist():
#     s = MultiStack(stack_size=3, number_of_stacks=1)
#     with pytest.raises(StackDoesNotExistError):
#         s.push(1, 1)



if __name__ == "__main__":
    super_stack = MultiStack()
    super_stack.push(1, 5)
    super_stack.push(2, 5)
    super_stack.push(3, 5)

    super_stack.push(1, 6)
    super_stack.push(2, 6)
    super_stack.push(3, 6)

    super_stack.push(1, 7)
    super_stack.push(2, 7)
    super_stack.push(3, 7)


    print(super_stack.arr, super_stack.d)