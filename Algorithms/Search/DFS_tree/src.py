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

                  8
                 /\
                /  \
              2     6
             /\      \
            /  \      \
           2    6      1
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


def depth_first_search(tree_head, key):
    if tree_head is None:
        return False
    
    if tree_head.value == key:
        return True

    if depth_first_search(tree_head.left, key):
        return True

    if depth_first_search(tree_head.right, key):
        return True

    return False


if __name__ == "__main__":
    tree = create_sample_tree()
    print(depth_first_search(tree, 10))

