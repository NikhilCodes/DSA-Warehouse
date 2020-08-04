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


if __name__ == '__main__':
    g = Graph()
    g.add_edge('a', 'b', 3)
    g.add_edge('a', 'c', 2)
    print(g.get_neighbours('b'))
    print(g.data)
