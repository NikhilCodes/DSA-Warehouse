class BinarySearchTree:

    class Node:

        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def __repr__(self):
            return f"[{self.value}]"

        def get_successor_value(self, pop=False):
            if self.right is None:
                return None

            successor_value = self.right.value
            working_node = self.right
            parent_node = self
            while working_node.left:
                parent_node = working_node
                working_node = working_node.left
                successor_value = working_node.value

            if pop:
                if parent_node is self:
                    parent_node.right = None
                else:
                    parent_node.left = None

            return successor_value

    tree = None

    def __init__(self, iterable):
        if len(iterable) == 0:
            return

        self.tree = self.Node(iterable[0])
        if len(iterable) == 1:
            return

        for element in iterable[1:]:
            self.insert(element)

    def __repr__(self):
        def in_order_traversal(tree):
            if self is None:
                return "[Empty BST]"

            left = None
            right = None

            if tree.left:
                left = in_order_traversal(tree.left)
            if tree.right:
                right = in_order_traversal(tree.right)

            subtree = []
            if left is not None:
                subtree.append(str(left))
            subtree.append(str(tree))
            if right is not None:
                subtree.append(str(right))

            return '-'.join(subtree)
        return in_order_traversal(self.tree)

    def insert(self, value):
        working_node = self.tree
        while True:
            if working_node.value == value:
                break
            elif working_node.value > value:
                if working_node.left is None:
                    working_node.left = self.Node(value)
                    break

                working_node = working_node.left
            else:
                if working_node.right is None:
                    working_node.right = self.Node(value)
                    break

                working_node = working_node.right

    def search(self, value):
        working_node = self.tree

        while working_node:
            if working_node.value == value:
                return True

            elif value < working_node.value:
                working_node = working_node.left
            else:
                working_node = working_node.right

        return False

    def delete(self, value):
        parent_node = None
        working_node = self.tree

        while working_node:
            if working_node.value == value:
                break

            elif value < working_node.value:
                parent_node = working_node
                working_node = working_node.left
            else:
                parent_node = working_node
                working_node = working_node.right

        if working_node is None:
            raise Exception("Couldn't find element to be deleted.")

        if working_node.left is None and working_node.right is None:  # Case: 1 (NO CHILD NODES)
            if parent_node.left == working_node:
                parent_node.left = None
            else:
                parent_node.right = None
        elif working_node.left or working_node.right:  # Case: 2 (ONE CHILD NODE)
            if parent_node.left == working_node:
                if working_node.left:
                    parent_node.left = working_node.left
                else:
                    parent_node.left = working_node.right
            else:
                if working_node.left:
                    parent_node.right = working_node.left
                else:
                    parent_node.right = working_node.right
        else:  # Case: 3 (TWO CHILD NODES)
            successor_val = working_node.get_successor_value(pop=True)
            working_node.value = successor_val


if __name__ == '__main__':
    BST = BinarySearchTree([4, 2, 6, 1, 0, 3, 7])
    BST.delete(2)
    print(BST, BST.search(7))
