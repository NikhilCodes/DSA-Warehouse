class SinglyLinkedList {
    class Node {
        int value;
        Node next;

        Node(int n) { this.value = n; }
    }

    Node head, tail;

    void addElement(int value) {
        if(this.head == null) {
            this.head = new Node(value);
            this.tail = this.head;
        } else {
            this.tail.next = new Node(value);
            this.tail = this.tail.next;
        }
    }

    void displayList() {
        Node workingNode = this.head;
        while(workingNode != null) {
            System.out.printf("[%d] ", workingNode.value);
            workingNode = workingNode.next;
        }
    }
}

class SRC {
    public static void main(String[] args) {
        SinglyLinkedList ll = new SinglyLinkedList();
        ll.addElement(3);
        ll.addElement(6);
        ll.addElement(9);
        ll.addElement(12);
        ll.displayList();
        System.out.println();
    }
}