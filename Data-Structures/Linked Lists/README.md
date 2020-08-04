# Linked Lists
A linked list is a linear collection of data elements, whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists.

## Types of Linked Lists
- **Singly Linked List**
   
    Singly linked lists contain nodes which have a data field as well as 'next' field, which points to the next node in line of nodes.

    ![Singly Linked List Visual](/resources/singly-linked-list.png)

- **Doubly Linked List**
   
    In a 'doubly linked list', each node contains, besides the next-node link, a second link field pointing to the 'previous' node in the sequence. The two links may be called 'forward('s') and 'backwards', or 'next' and 'prev'('previous').



    ![Doubly Linked List Visual](/resources/doubly-linked-list.png)

- **Circular Linked List**
   
    In the case of a circular linked list, the last node points to the first node of the list, hence making it a cycle.

    ![Circular Linked List Visual](/resources/circular-linked-list.png)

- **XOR Linked List**
   
    An XOR linked list is a type of data structure used in computer programming. It takes advantage of the bitwise XOR operation to decrease storage requirements for doubly linked lists.

    ![XOR Linked List Visual](/resources/xor-linked-list.png)
