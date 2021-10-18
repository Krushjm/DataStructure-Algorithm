from __future__ import annotations

from typing import List, Optional


class CircularListNode:
    def __init__(self, val: int, n: CircularListNode = None):
        self.val = val
        self.next = n


class CircularLinkedList:
    """
    Peek: O(n)
    Insert / Delete:
        (only work on element after cursor): O(1)
    """
    def __init__(self, values: List[int]):
        self.cursor: Optional[CircularListNode] = None
        self.length = 0
        self.construct_list(values)

    def construct_list(self, values: List[int]):
        if not values:
            raise ValueError('Empty list!')

        for v in values:
            self.add_node(v)

    def add_node(self, v):
        """Insert a new node after cursor.
           If the list is empty, then new node becomes cursor
           and it's next point to itself."""
        node = CircularListNode(v)
        if self.cursor is None:
            node.next = node
            self.cursor = node
        else:
            node.next = self.cursor.next
            self.cursor.next = node
        self.length += 1

    def remove_node(self):
        """Remove and return the node after the cursor (not the
           cursor itself, unless it is the only node).
           If the list become to empty, set cursor to null."""
        if self.cursor is None:
            print('List is empty!')
        elif self.cursor.next == self.cursor:
            self.cursor = None
            self.length -= 1
        else:
            self.cursor.next = self.cursor.next.next
            self.length -= 1

    def forward(self):
        self.cursor = self.cursor.next

    def traverse(self):
        if self.cursor:
            node = self.cursor
            while self.cursor.next != node:
                print(self.cursor.val)
                self.forward()
            print(self.cursor.val)


if __name__ == '__main__':
    cll = CircularLinkedList([1, 4])

    cll.add_node(3)
    cll.traverse()
    print('length: ', cll.length)

    cll.remove_node()
    cll.remove_node()
    cll.remove_node()
    cll.remove_node()
    cll.traverse()
    print('length: ', cll.length)

