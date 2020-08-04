class SinglyLinkedList:

    class Node:

        def __init__(self, value=None):
            self.value = value
            self.nextNode = None

        def __repr__(self):
            return "[{}]".format(self.value)

    def __init__(self, iterable):
        """
        Time Complexity : O(n)
        """
        if len(iterable) == 0:
            self.headNode = None
            self.tailNode = None
            return

        self.headNode = self.Node(iterable[0])
        self.tailNode = self.Node(iterable[-1])

        node = self.headNode
        for element in iterable[1:]:
            node.nextNode = self.Node(element)
            node = node.nextNode

    def __repr__(self):
        """
        Time Complexity : O(n)
        """
        node = self.headNode
        if node is None:
            return "EmptyLinkedList"

        display_str = ["[" + str(node.value) + "]"]

        while node.nextNode is not None:
            node = node.nextNode
            display_str.append(str(node))

        return '->-'.join(display_str)

    def prepend(self, value):
        """
        Time Complexity : O(1)
        """
        new_node = self.Node(value)
        if self.tailNode is None:
            self.tailNode = new_node

        new_node.nextNode = self.headNode
        self.headNode = new_node
        del new_node

    def append(self, value):
        """
        Time Complexity : O(1)
        """
        new_node = self.Node(value)
        if self.tailNode is None:
            self.tailNode = new_node
            return

        self.tailNode.nextNode = new_node
        self.tailNode = new_node

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
            raise Exception("Insertion position mut be within the LinkedList.")

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

    def search(self, item):
        working_node = self.headNode
        while working_node:
            if item == working_node.value:
                return True
            working_node = working_node.nextNode

        return False


if __name__ == '__main__':
    linked_list = SinglyLinkedList([])
    print(linked_list)
    linked_list.prepend(2)
    linked_list.append(7)
    linked_list.insert(6, 0)
    print(linked_list)
    print("Size:", linked_list.size())
    print("Node at Position 2:", linked_list.get_node_at_position(2))
    key = 2
    print(f"Node [{key}] is present: {linked_list.search(key)}")
