from binary_search_tree import BinarySearchTree


def in_order_successor(input_node):
    if input_node == None:
        return None

    if input_node.right:
        return find_left_node(input_node.right)

    temp = input_node
    x = temp.parent

    while x != None and x.left != temp:
        temp = x
        x = x.parent

    return x


def find_left_node(node):
    if node == None:
        return None

    while node.left != None:
        node = node.left

    return node



def test_in_order_successor():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Test all nodes
    inputs = [5, 9, 11, 12, 14, 20, 25]
    outputs = inputs[1:]
    outputs.append(None)

    for x, y in zip(inputs, outputs):
        test = bst.get_node(x)
        succ = in_order_successor(test)
        if succ is not None:
            assert succ.key == y
        else:
            assert succ == y


if __name__ == "__main__":
    test_in_order_successor()