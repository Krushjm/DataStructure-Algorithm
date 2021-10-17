from __future__ import annotations

from typing import List


class SinglyListNode:
    def __init__(self, val: int, n: SinglyListNode = None):
        self.val = val
        self.next = n


class SinglyLinkedList:
    """
    Peek: O(n)
    Insert / Delete:
        Beginning: O(1)
        End: O(n)
        Middle: [Peek] + O(1)
    """
    def __init__(self, values: List[int], mode: str = 'tail'):
        self.head = SinglyListNode(0)
        self.tail = self.head
        self.construct_list(values=values, mode=mode)

    def construct_list(self, values: List[int], mode: str):
        if not values:
            raise ValueError('Empty list!')

        for v in values:
            node = SinglyListNode(v)
            if mode == 'tail':
                self.add_tail(node)
            elif mode == 'head':
                self.add_head(node)
            else:
                raise ValueError('Wrong construct mode, only support "head" and "tail"!')

    def add_tail(self, node):
        self.tail.next, self.tail = node, node

    def add_head(self, node):
        node.next, self.head.next = self.head.next, node
        self.tail = node if self.head == self.tail else self.tail

    def remove_head(self):
        if not self.head == self.tail:
            self.head.next = self.head.next.next
            if self.head.next is None:
                self.tail = self.head

    def remove_tail(self):
        if not self.head == self.tail:
            node = self.head
            while node.next != self.tail:
                node = node.next
            self.tail, node.next = node, None

    def traverse(self):
        node = self.head.next
        while node:
            print(node.val)
            node = node.next


if __name__ == '__main__':
    sll = SinglyLinkedList([1, 2, 3, 4], 'head')
    print(sll.head.next.val)
    print(sll.tail.val)

    sll.remove_head()
    sll.traverse()

    sll.remove_tail()
    sll.remove_tail()
    sll.traverse()
