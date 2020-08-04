class PriorityQueue:
    """ Lesser the `priority_lvl` integer greater the priority. """
    class Node:
        def __init__(self, value):
            self.value = value
            self.priority_lvl = None
            self.nextNode = None

        def __repr__(self):
            return "[{}]".format(self.value)

    def __init__(self):
        self.firstNode = None
        self.lastNode = None

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

    def add(self, value, priority):
        new_node = self.Node(value)
        new_node.priority_lvl = priority

        if self.firstNode is None:
            self.firstNode = self.lastNode = new_node
        elif self.firstNode.priority_lvl > priority:
            new_node.nextNode = self.firstNode
            self.firstNode = new_node
        elif self.firstNode.priority_lvl <= priority and self.firstNode.nextNode is None:
            self.firstNode.nextNode = new_node
            self.lastNode = new_node
        else:
            worker_parent_node = self.firstNode
            worker_node = self.firstNode.nextNode

            while priority > worker_node.priority_lvl:
                worker_node = worker_node.nextNode
                worker_parent_node = worker_parent_node.nextNode

                if worker_node is None:
                    worker_parent_node.nextNode = new_node
                    self.lastNode = new_node
                    return

            new_node.nextNode = worker_node
            worker_parent_node.nextNode = new_node

    def remove(self):
        self.firstNode = self.firstNode.nextNode
        if self.firstNode is None:
            self.lastNode = None


if __name__ == '__main__':
    queue = PriorityQueue()
    queue.add(3, priority=3)
    queue.add(5, priority=0)
    queue.add(1, priority=5)

    print(queue)

    queue.remove()
    queue.remove()

    print(queue.lastNode)