class Graph:
    def __init__(self):
        self.data = dict()

    def add_edge(self, start, end, weight):
        # Establishing Bidirectional Path
        if self.data.get(start):
            self.data[start].add((end, weight))
        else:
            self.data[start] = {(end, weight)}

        if self.data.get(end):
            self.data[end].add((start, weight))
        else:
            self.data[end] = {(start, weight)}

    def get_neighbours(self, value):
        return self.data.get(value)

    def exists(self, value):
        if self.data.get(value):
            return True

        return False


# Helper Function and Classes Defined here
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
        return self.firstNode

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

    def pop(self):
        tmp = self.firstNode
        self.firstNode = self.firstNode.nextNode
        if self.firstNode is None:
            self.lastNode = None

        return tmp
##


# Defining Dijkstra Algorithm
def dijkstra(graph: Graph, start, end):
    if not(graph.exists(start) and graph.exists(end)):
        raise Exception("Start or End does not exist inside the graph.")

    solution = {
        start: [0, None]
    }

    if start == end:
        return start

    visited_nodes = set()
    nodes_to_visit_ordered_priority_wise = PriorityQueue()
    nodes_to_visit_ordered_priority_wise.add(start, priority=0)

    while True:
        if nodes_to_visit_ordered_priority_wise.peek().value == end:
            break

        _buffer_elem: PriorityQueue.Node = nodes_to_visit_ordered_priority_wise.peek()
        _buffer_set: set = graph.get_neighbours(_buffer_elem.value)
        visited_nodes.add(_buffer_elem.value)
        nodes_to_visit_ordered_priority_wise.pop()

        for i in _buffer_set:
            if i[0] not in visited_nodes:
                if solution.get(i[0]) is None or solution[i[0]][0] > i[1] + _buffer_elem.priority_lvl:
                    solution[i[0]] = [i[1] + _buffer_elem.priority_lvl, _buffer_elem.value]

                nodes_to_visit_ordered_priority_wise.add(i[0], i[1] + solution[_buffer_elem.value][0])

    # Backtracking
    parent = end
    dist = solution[end][0]
    path = []
    while parent is not None:
        path.append(parent)
        parent = solution[parent][1]

    path.reverse()

    return path, dist


if __name__ == '__main__':
    g = Graph()

    g.add_edge((0,0), (0,1), 1)
    g.add_edge((0,0), (1,0), 1)
    g.add_edge((0,0), (1,1), 1)
    print(dijkstra(g, (0,0), (1,1)))

    g.add_edge('a', 'b', 5)
    g.add_edge('b', 'c', 1)
    g.add_edge('a', 'c', 3)
    g.add_edge('a', 'd', 1)
    g.add_edge('d', 'e', 2)
    g.add_edge('c', 'e', 6)

    print(dijkstra(g, 'b', 'd'))
    # b c a d

    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    print(dijkstra(g, 0, 4))
    # 0 7 6 5 4
