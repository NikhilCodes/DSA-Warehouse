class DoublyLinkedList:

    class Node:

        def __init__(self, value):
            self.value = value
            self.prevNode = None
            self.nextNode = None

        def __repr__(self):
            return "[{}]".format(self.value)

    def __init__(self, iterable):
        if len(iterable) == 0:
            self.headNode = None
            return

        self.headNode = self.Node(iterable[0])

        node = self.headNode
        for element in iterable[1:]:
            node.nextNode = self.Node(element)
            node.nextNode.prevNode = node
            node = node.nextNode

    def __repr__(self):
        """
        Time Complexity : O(n)
        """
        node = self.headNode
        if node is None:
            return "EmptyDoublyLinkedList"

        display_str = ["[" + str(node.value) + "]"]

        while node.nextNode is not None:
            node = node.nextNode
            display_str.append(str(node))

        return '-><-'.join(display_str)

    def prepend(self, value):
        """
        Time Complexity : O(1)
        """
        new_node = self.Node(value)
        new_node.nextNode = self.headNode
        self.headNode = new_node
        del new_node

    def append(self, value):
        """
        Time Complexity : O(n)
        """
        new_node = self.Node(value)
        working_node = self.headNode
        while working_node.nextNode is not None:
            working_node = working_node.nextNode

        working_node.nextNode = new_node
        del working_node

    def size(self):
        """
        Time Complexity : O(n)
        """
        length = 0
        if self.headNode is None:
            return 0

        if self.headNode.value is not None:
            length = 1

        working_node = self.headNode
        while working_node.nextNode is not None:
            length += 1
            working_node = working_node.nextNode

        del working_node
        return length

    def insert(self, value, position):
        """
        Time Complexity : O(k)
        (k represents position)
        """
        if self.size() < position:
            raise Exception("Insertion position mut be within the DoublyLinkedList.")

        if position == 0:
            self.prepend(value)
        else:
            new_node = self.Node(value)
            working_node = self.headNode
            for i in range(position-1):
                working_node = working_node.nextNode

            new_node.nextNode = working_node.nextNode
            working_node.nextNode = new_node

    def get_node_at_position(self, position):
        working_node = self.headNode
        for i in range(position):
            working_node = working_node.nextNode

        return working_node


if __name__ == "__main__":
    d_linked_list = DoublyLinkedList([3, 4])
    d_linked_list.insert(9, 1)
    print(d_linked_list)
