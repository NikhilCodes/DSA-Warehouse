class Stack:

    topNode = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.nextNode = None

        def __repr__(self):
            return "[{}]".format(self.value)

    def __init__(self, iterable):
        if len(iterable) != 0:
            for k in iterable:
                new_node = self.Node(k)
                new_node.nextNode = self.topNode
                self.topNode = new_node

    def __repr__(self):
        lines = []
        working_node = self.topNode
        if working_node is None:
            return "[EmptyStack]"

        while working_node is not None:
            lines.append(str(working_node))
            working_node = working_node.nextNode

        return "\n |\n".join(lines)

    def peek(self):
        return self.topNode.value

    def push(self, value):
        new_node = self.Node(value)
        new_node.nextNode = self.topNode
        self.topNode = new_node

    def pop(self):
        self.topNode = self.topNode.nextNode

    def is_empty(self):
        if self.topNode is None:
            return True

        return False


if __name__ == '__main__':
    stack = Stack([3, 5])

    stack.push(6)
    stack.pop()

    print(stack)

    stack.pop()
    stack.pop()

    print(stack, stack.is_empty())
