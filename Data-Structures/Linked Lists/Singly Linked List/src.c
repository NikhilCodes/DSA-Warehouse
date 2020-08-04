#include <stdlib.h>
#include <stdio.h>

struct Node {
    int value;
    struct Node *next;
};

void prepend(struct Node **head, int value) {
    // Time Complexity: O(1)

    struct Node *newNode = (struct Node *) malloc(sizeof(struct Node));
    newNode->value = value;
    newNode->next = *head;
    *head = newNode;
}

void append(struct Node **head, int value) {
    // Time Complexity: O(n)
    // Can be optimized to `O(1)` by tracking LinkedListTail
    struct Node *newNode = (struct Node *) malloc(sizeof(struct Node));
    newNode->value = value;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    struct Node *lastNode = *head;

    while (lastNode->next != NULL) {
        lastNode = lastNode->next;
    }

    lastNode->next = newNode;
}

void displayLinkedList(struct Node *head) {
    if (head == NULL) {
        return;
    }
    struct Node *currNode = head;
    printf("[%d]", currNode->value);
    currNode = currNode->next;
    while (currNode != NULL) {
        printf("-[%d]", currNode->value);
        currNode = currNode->next;
    }
    printf("\n");
}

int main() {
    struct Node *linkedListHead = NULL;
    prepend(&linkedListHead, 5);
    prepend(&linkedListHead, 3);
    prepend(&linkedListHead, 7);
    prepend(&linkedListHead, 1);

    append(&linkedListHead, 9);

    displayLinkedList(linkedListHead);
    return 0;
}