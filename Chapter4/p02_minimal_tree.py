class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.val}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()



def array_to_binary_tree(arr, start, end):
    # n  and 2n and 2n+1
    if len(arr) == 0:
        return None

    if start > end:
        return None

    mid = (start + end) // 2

    if mid >= len (arr):
        return None
    print(arr[mid])
    root = Node(arr[mid])
    print(arr)
    root.left = array_to_binary_tree(arr, start, mid-1)
    root.right = array_to_binary_tree(arr, mid+1, end)
    return root



if __name__ == "__main__":
    test_array = [1,2,3,4,5,6,7,8,9,10]
    # test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    root = array_to_binary_tree(test_array, 0, len(test_array))
    print(root.__str__())