class Queue:

    firstNode = None
    lastNode = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.nextNode = None

        def __repr__(self):
            return "[{}]".format(self.value)

    def __init__(self, iterable):
        if len(iterable) != 0:
            self.firstNode = self.lastNode = self.Node(iterable[0])

            working_node = self.firstNode
            for k in iterable[1:]:
                new_node = self.Node(k)
                self.lastNode = new_node
                working_node.nextNode = new_node
                working_node = working_node.nextNode

    def __repr__(self):
        lines = []
        working_node = self.firstNode
        if working_node is None:
            return "[EmptyQueue]"

        while working_node is not None:
            lines.append(str(working_node))
            working_node = working_node.nextNode

        return "--".join(lines)

    def is_empty(self):
        if self.firstNode is None:
            return True

        return False

    def peek(self):
        return self.firstNode.value

    def add(self, value):
        if self.firstNode is None:
            self.firstNode = self.lastNode = self.Node(value)
        else:
            self.lastNode.nextNode = self.Node(value)
            self.lastNode = self.lastNode.nextNode

    def remove(self):
        self.firstNode = self.firstNode.nextNode
        if self.firstNode is None:
            self.lastNode = None


if __name__ == '__main__':
    queue = Queue([2, 9])
    queue.add(3)
    queue.add(5)

    print(queue)

    queue.remove()
    queue.remove()

    print(queue.lastNode)
