from collections import deque

from Chapter2.linked_list import LinkedListNode
from Chapter2.linked_list import LinkedList


class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def create_node_list_by_depth(tree_root):
    if tree_root == None:
        return []

    arr = []


    level = 0

    if len(arr) <= level:
        node = LinkedListNode(tree_root)
        arr.append(node)


    def insert_values_at_level(node, height):
        if node == None:
            return

        if len(arr) <= height:
            node = LinkedListNode(tree_root)
            arr.append(node)
        else:

            def insert_values_at_linkedList(head, node):
                temp = head
                while temp.next != None:
                    temp = temp.next

                temp.next = LinkedListNode(node)

            insert_values_at_linkedList(arr[height], node)

        insert_values_at_level(node.left, height+1)
        insert_values_at_level(node.right, height+1)

    insert_values_at_level(tree_root.left, level+1)
    insert_values_at_level(tree_root.right, level+1)

    return arr

#
def create_node_list_by_depth_b(tree):
    
    return


testable_functions = [create_node_list_by_depth, ]


def test_create_node_list_by_depth():
    for f in testable_functions:
        node_h = BinaryNode("H")
        node_g = BinaryNode("G")
        node_f = BinaryNode("F")
        node_e = BinaryNode("E", node_g)
        node_d = BinaryNode("D", node_h)
        node_c = BinaryNode("C", None, node_f)
        node_b = BinaryNode("B", node_d, node_e)
        node_a = BinaryNode("A", node_b, node_c)
        lists = f(node_a)

        assert lists[0].values() == LinkedList([node_a]).values()
        assert lists[1].values() == LinkedList([node_b, node_c]).values()
        assert lists[2].values() == LinkedList([node_d, node_e, node_f]).values()
        assert lists[3].values() == LinkedList([node_h, node_g]).values()


def example():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = create_node_list_by_depth(root)
    print(levels)


if __name__ == "__main__":
    example()