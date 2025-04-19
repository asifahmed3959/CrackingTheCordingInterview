from binary_tree import BinaryTree



def first_common_ancestor(p, q):
    if not p or not q:
        return None
    depth_p = get_depth(p)
    depth_q = get_depth(q)
    delta = abs(depth_p - depth_q)
    if depth_p < depth_q:
        for _ in range(delta):
            q = q.parent
    elif depth_q < depth_p:
        for _ in range(delta):
            p = p.parent
    ancestor_p = p
    ancestor_q = q
    while ancestor_p != ancestor_q:
        ancestor_p = ancestor_p.parent
        ancestor_q = ancestor_q.parent
    return ancestor_p


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth


if __name__ == "__main__":
    t
    

    ancestor = first_common_ancestor(n3, n4)
    print(ancestor.key)