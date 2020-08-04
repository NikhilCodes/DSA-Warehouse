class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"[{self.value}]"


def create_sample_tree():
    r"""
        Structure should be:

                node1
                 /\
                /  \
            node2  node3
             /\      \
            /  \      \
        node4  node5  node6
    """

    node1 = Node(8)
    node2 = Node(2)
    node3 = Node(6)
    node4 = Node(2)
    node5 = Node(6)
    node6 = Node(1)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6

    return node1


def in_order_traverse(tree_node):
    if tree_node is None:
        return

    if tree_node.left:
        in_order_traverse(tree_node.left)

    print(tree_node, end=' ')

    if tree_node.right:
        in_order_traverse(tree_node.right)
    elif tree_node.left:
        print("[None]")


if __name__ == '__main__':
    tree = create_sample_tree()
    in_order_traverse(tree)
