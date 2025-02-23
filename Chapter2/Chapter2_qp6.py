import time

from linked_list import LinkedList
from linked_list import LinkedListNode


def is_palindrome(ll):
    arr = []
    temp = ll.head

    while temp != None:
        arr.append(temp.value)
        temp = temp.next

    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j-= 1

    return True



def is_palindrome_constant_space(ll):
    temp = reverse(ll.head)

    curr = ll.head

    while curr != None:
        if curr.value != temp.value:
            return False

        temp = temp.next
        curr = curr.next

    return True




def reverse(node):
    """
    reverses a linked list,
    returns the input list's
    tail node as the new head

        Time : O(N)
        Space: O(1)
    """
    previous_node = None
    curr = node

    while curr != None:
        temp = LinkedListNode(curr.value, None)
        temp.next = previous_node
        previous_node = temp
        curr = curr.next

    return previous_node




# def is_palindrome_recursive(ll):
#     def get_len(node):
#         if not node:
#             return 0
#         else:
#             return 1 + get_len(node.next)
#
#     def recursive_transverse(node, length):
#         if not node or length == 0:  # even list
#             return True, node
#         elif length == 1:  # odd list
#             return True, node.next
#
#         _is_palindrome, fwd_node = recursive_transverse(node.next, length - 2)
#
#         if not _is_palindrome or not fwd_node:
#             return False, None
#
#         if node.value == fwd_node.value:
#             return True, fwd_node.next
#         else:
#             return False, None
#
#     return recursive_transverse(ll.head, get_len(ll.head))[0]


test_cases = [
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1], True),
    (["a", "a"], True),
    ("aba", True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2], False),
]

testable_functions = [
    is_palindrome,
    is_palindrome_constant_space,
    # is_palindrome_recursive,
]


def test_is_palindrome():
    for f in testable_functions:
        start = time.perf_counter()
        for values, expected in test_cases:
            print(f"{f.__name__}: {values}")
            for _ in range(100):
                assert f(LinkedList(values)) == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    test_is_palindrome()