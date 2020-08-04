class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"[{self.value}]"

    def copy_node(self, node):
        self.value = node.value
        self.left = node.left
        self.right = node.right

    def rotate_left(self):
        new_root = Node(None)
        new_root.copy_node(self.right)
        prev_root = Node(None)
        prev_root.copy_node(self)

        prev_root.right = new_root.left
        new_root.left = prev_root

        self.copy_node(new_root)

    def rotate_right(self):
        new_root = Node(None)
        new_root.copy_node(self.left)
        prev_root = Node(None)
        prev_root.copy_node(self)

        prev_root.left = new_root.right
        new_root.right = prev_root

        self.copy_node(new_root)

    def in_order_display_tree(self):  # In Order traversal of the tree
        if self is None:
            print(None)
            return

        if self.left:
            self.left.in_order_display_tree()
        elif self.right:
            print(None, end=' ')
        print(self, end=' ')
        if self.right:
            self.right.in_order_display_tree()
        elif self.left:
            print(None, end=' ')

    def post_order_display_tree(self):  # Post Order traversal of the tree
        if self is None:
            print(None)
            return

        if self.left:
            self.left.post_order_display_tree()

        if self.right:
            self.right.post_order_display_tree()
        elif self.left:
            print(None, end=' ')

        print(self, end=' ')


if __name__ == "__main__":
    node1 = Node(4)
    node2 = Node(2)
    node3 = Node(6)
    node4 = Node(1)
    node5 = Node(3)
    node6 = Node(5)
    node7 = Node(7)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    r"""
    Structure should be:
            
             4
             /\
            /  \
          2     6
         /\    / \ 
        /  \  5   \
       1    3      7
    
    """

    node1.in_order_display_tree()
