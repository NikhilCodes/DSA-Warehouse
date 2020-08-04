class XORLinkedList:
    MEMORY = dict()

    class Node:
        def __init__(self, value):
            self.value = value
            self.both = None

        def __repr__(self):
            return "[{}]".format(self.value)

    def __init__(self, iterable):
        head_node = self.Node(iterable[0]) if len(iterable) != 0 else None
        second_node = self.Node(iterable[1]) if len(iterable) > 1 else None

        self.endNodeAddr = None
        self.beforeEndNodeAddr = None

        if head_node:
            self.headNodeAddr = id(head_node)
            self.MEMORY[self.headNodeAddr] = head_node
            self.endNodeAddr = self.headNodeAddr
        else:
            self.headNodeAddr = None

        if second_node:
            self.secondNodeAddr = id(second_node)
            self.MEMORY[self.secondNodeAddr] = second_node
            self.endNodeAddr = self.secondNodeAddr
            self.beforeEndNodeAddr = self.headNodeAddr
        else:
            self.secondNodeAddr = None

        curr = self.MEMORY.get(self.secondNodeAddr)
        prev = self.MEMORY.get(self.headNodeAddr)

        for k in iterable[2:]:
            new_node = self.Node(k)
            new_node_addr = id(new_node)
            curr.both = new_node_addr ^ id(prev)
            self.MEMORY[new_node_addr] = new_node
            prev = curr
            curr = new_node

        self.endNodeAddr = id(curr)
        self.beforeEndNodeAddr = id(prev)

    def __repr__(self):
        xor_ll = []
        head_node = self.MEMORY.get(self.headNodeAddr)
        second_node = self.MEMORY.get(self.secondNodeAddr)
        if head_node:
            xor_ll.append(str(head_node))
        else:
            return "EmptyXORLinkedList"

        if second_node:
            xor_ll.append(str(second_node))
        else:
            return str(head_node)

        prev = head_node
        curr = second_node
        next_node = self.MEMORY.get(id(prev) ^ curr.both) if curr.both else None
        while next_node:
            xor_ll.append(str(next_node))
            prev = curr
            curr = next_node
            next_node = self.MEMORY.get(id(prev) ^ curr.both) if curr.both else None

        return "-xor-".join(xor_ll)

    def add(self, value):
        new_node = self.Node(value)
        new_node_addr = id(new_node)
        self.MEMORY[new_node_addr] = new_node
        if self.headNodeAddr is None:
            self.headNodeAddr = self.endNodeAddr = new_node_addr
            return
        elif self.secondNodeAddr is None:
            self.beforeEndNodeAddr = self.headNodeAddr
            self.secondNodeAddr = self.endNodeAddr = new_node_addr
            return

        end_node = self.MEMORY[self.endNodeAddr]
        end_node.both = self.beforeEndNodeAddr ^ new_node_addr
        self.beforeEndNodeAddr = self.endNodeAddr
        self.endNodeAddr = new_node_addr

    def get(self, index):
        head_node = self.MEMORY.get(self.headNodeAddr)
        second_node = self.MEMORY.get(self.secondNodeAddr)
        if index == 0 and head_node:
            return head_node

        if index == 1 and second_node:
            return second_node

        prev = head_node
        curr = second_node
        next_node = self.MEMORY.get(id(prev) ^ curr.both) if curr.both else None
        i = 2
        while next_node:
            if i == index:
                return next_node
            prev = curr
            curr = next_node
            next_node = self.MEMORY.get(id(prev) ^ curr.both) if curr.both else None
            i += 1

    def search(self, key):
        head_node = self.MEMORY.get(self.headNodeAddr)
        second_node = self.MEMORY.get(self.secondNodeAddr)

        if head_node.value == key:
            return True
        if second_node is not None:
            if second_node.value == key:
                return True
        else:
            return False

        prev = head_node
        curr = second_node
        next_node = self.MEMORY.get(id(prev) ^ curr.both) if curr.both else None

        while next_node:
            if next_node.value == key:
                return True

            prev = curr
            curr = next_node
            next_node = self.MEMORY.get(id(prev) ^ curr.both) if curr.both else None

        return False


if __name__ == "__main__":
    xor_l = XORLinkedList([])
    xor_l.add(5)
    xor_l.add(8)
    xor_l.add(2)
    xor_l.add(1)
    print(xor_l)
    print("Element at index 2 : {}".format(xor_l.get(2)))
    key = 5
    print(f"Node [{key}] is present: {xor_l.search(key)}")
