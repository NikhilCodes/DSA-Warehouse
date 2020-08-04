class CircularLinkedList:
     
    headNode = None
    lastNode = None
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.nextNode = None

        def __repr__(self):
            return f"[{self.value}]"

    def __init__(self, iterable):
        for element in iterable:
            self.add(element)
    
    def __repr__(self):
        curr_node = self.headNode
        line = [str(curr_node)]
        while curr_node is not None and curr_node is not self.lastNode:
            curr_node = curr_node.nextNode
            line.append(str(curr_node))

        return '-'.join(line)

    def add(self, value):
        new_node = self.Node(value)
        if self.headNode is None:
            self.headNode = new_node
            self.headNode.nextNode = self.headNode
            self.lastNode = self.headNode
            return
        
        self.lastNode.nextNode = new_node
        new_node.nextNode = self.headNode
        self.lastNode = new_node


if __name__ == "__main__":
    c_ll = CircularLinkedList([8, 2])
    c_ll.add(4)
    c_ll.add(9)
    print(c_ll.headNode.nextNode)
    print(c_ll)
