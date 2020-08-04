class Trie:
    class Node:
        def __init__(self, value):
            self.value = value
            self.nextNodes = list()

        def __repr__(self):
            return f"{self.value}"

        def in_next_node_by_value(self, node):
            for n in self.nextNodes:
                if n.value == node.value:
                    return True

            return False

        def get_index_in_next_node_by_value(self, node):
            index = 0
            for n in self.nextNodes:
                if n.value == node.value:
                    return index

                index += 1

    def __init__(self, iterable=None):
        self.headNode = self.Node("*")

        if iterable is None:
            return

        for k in iterable:
            self.add(k)

    def add(self, string):
        working_node = self.headNode
        for l in string:
            new_node = self.Node(l)
            if not working_node.in_next_node_by_value(new_node):
                working_node.nextNodes.append(new_node)
                working_node = new_node
                continue

            working_node = working_node.nextNodes[working_node.get_index_in_next_node_by_value(new_node)]
        working_node.nextNodes.append(self.Node("#"))  # End Node


if __name__ == '__main__':
    trie = Trie(['deer', 'dog', 'deep', 'area', ])
    r"""
    Resulting Trie structure is:
                
                *
               / \
              d   a
             / \   \
            e   o   r
           /     \   \
          e       g   e
         / \       \   \
        r   p       #   a
       /     \           \
      #       #           #
    """
