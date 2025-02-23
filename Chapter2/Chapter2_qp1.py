import time

from linked_list import LinkedList
from linked_list import LinkedListNode


def remove_dups(ll):
    d = {}
    prev = LinkedListNode(0)
    prev.next = ll.head

    temp = ll.head

    while temp != None:
        if temp.value not in d:
            d[temp.value] = True
            prev.next = temp
            prev = prev.next
            temp = temp.next
        else:
            temp = temp.next

    prev.next = None
    return ll



def remove_dups_followup(ll):
    curr = ll.head

    while curr != None:
        prev = curr
        temp = curr.next

        while temp != None:
            if temp.value == curr.value:
                temp = temp.next
            else:
                prev.next = temp
                prev = prev.next
                temp = temp.next

        prev.next = None
        curr = curr.next
    return ll


testable_functions = (remove_dups, remove_dups_followup)
test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


def test_remove_dupes():
    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(100):
            for values, expected in test_cases:
                expected = expected.copy()
                deduped = f(LinkedList(values))
                assert deduped.values() == expected

                deduped.add(5)
                expected.append(5)
                assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


def example():
    ll = LinkedList.generate(20, 0, 9)
    print(ll)
    remove_dups(ll)
    print(ll)

    ll = LinkedList.generate(20
                             , 0, 9)
    print(ll)
    remove_dups_followup(ll)
    print(ll)


if __name__ == "__main__":
    example()