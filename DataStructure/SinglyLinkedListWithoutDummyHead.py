from __future__ import annotations

from typing import List, Optional


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
        self.head: Optional[SinglyListNode] = None
        self.tail: Optional[SinglyListNode] = None
        self.length = 0
        self.construct_list(values=values, mode=mode)

    def construct_list(self, values: List[int], mode: str):
        if not values:
            raise ValueError('Empty list!')

        for v in values:
            node = SinglyListNode(v)

            if self.head is None:
                self.head, self.tail = node, node
                self.length += 1
            else:
                if mode == 'tail':
                    self.add_tail(node)
                elif mode == 'head':
                    self.add_head(node)
                else:
                    raise ValueError('Wrong construct mode, only support "head" and "tail"!')

    def add_tail(self, node):
        self.tail.next, self.tail = node, node
        self.length += 1

    def add_head(self, node):
        node.next, self.head.next = self.head.next, node
        self.tail = node if self.head == self.tail else self.tail
        self.length += 1

    def remove_head(self):
        if self.head and self.head.next:
            self.head.next, self.head = None, self.head.next,
            self.length -= 1
        else:
            self.head, self.tail, = None, None

    def remove_tail(self):
        if self.head and self.head.next:
            node = self.head
            while node.next != self.tail:
                node = node.next
            self.tail, node.next, = node, None
            self.length -= 1
        else:
            self.head, self.tail = None, None

    def traverse(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next


if __name__ == '__main__':
    sll = SinglyLinkedList([1, 2, 3, 4])

    sll.remove_head()
    sll.traverse()
    print('length: ', sll.length)

    sll.remove_tail()
    sll.remove_tail()
    sll.traverse()
    print('length: ', sll.length)
