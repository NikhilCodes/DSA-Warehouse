from copy import copy


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


def breadth_first_search(tree_head, key, level=None):
    if level == set():
        return False

    if level is None:
        level = {tree_head}

    tmp_level = set()
    for i in level:
        if i.value == key:
            return True

        if i.left:
            tmp_level.add(i.left)
        if i.right:
            tmp_level.add(i.right)

    level = copy(tmp_level)

    if breadth_first_search(tree_head, key, level):
        return True
    return False


if __name__ == "__main__":
    tree = create_sample_tree()
    print(breadth_first_search(tree, 6))

