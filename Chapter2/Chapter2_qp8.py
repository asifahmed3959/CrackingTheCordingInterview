from linked_list import LinkedList


def loop_detection(ll):
    if ll.head == None:
        return False

    if ll.head.next == None:
        return False

    slow = ll.head
    fast = ll.head.next

    while fast != None and fast.next != None and slow != None:
        if fast == slow:
            return True

        fast = fast.next.next
        slow = slow.next
    return False


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), False),
        ((LinkedList((1, 2, 3))), False),
        (looped_list, True),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected