from linked_list import LinkedList


def kth_to_last(ll, k):
    temp = ll.head
    arr = []

    while temp != None:
        arr.append(temp)
        temp = temp.next
    return arr[-k]

#
# # O(N) space
def kth_last_recursive(ll, k):
    return_value, return_node = helper(ll.head, k)
    return return_node

def helper(node, k):
    if node == None:
        return 0, None

    return_value, return_node = helper(node.next, k)

    if return_value == k:
        return return_value, return_node

    return 1+return_value, node





test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected
        assert kth_last_recursive(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()