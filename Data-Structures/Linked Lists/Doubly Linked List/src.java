class DoublyLinkedList {
    class Node {
        int value;
        Node next, prev;

        Node(int n) { this.value = n; }
    }

    Node head, tail;
    private Node _oldTail;

    void addElement(int value) {
        Node newNode = new Node(value);
        if(this.head == null) {
            this.head = this.tail = this._oldTail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = this.tail.next;
            this.tail.prev = this._oldTail;
            this._oldTail = this.tail;
        }
    }
}

class SRC {
    public static void main(String args[]) {
        DoublyLinkedList dll = new DoublyLinkedList();
        dll.addElement(3);
        dll.addElement(6);
        dll.addElement(9);
        dll.addElement(12);

        System.out.println(dll.head.next.next.prev.value);
    }
}