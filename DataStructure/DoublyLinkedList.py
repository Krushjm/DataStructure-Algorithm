from __future__ import annotations

from typing import List


class DoublyListNode:
    def __init__(self, val: int, p: DoublyListNode = None, n: DoublyListNode = None):
        self.val = val
        self.prev = p
        self.next = n


class DoublyLinkedList:
    """
    Peek: O(n)
    Insert / Delete:
        Beginning: O(1)
        End: O(1)
        Middle: [Peek] + O(1)
    """
    def __init__(self, values: List[int], mode: str = 'tail'):
        self.head = DoublyListNode(0)
        self.tail = DoublyListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.length = 0
        self.construct_list(values, mode)

    def construct_list(self, values: List[int], mode: str):
        if not values:
            raise ValueError('Empty list!')

        for v in values:
            node = DoublyListNode(v)
            if mode == 'head':
                self.add_head(node)
            elif mode == 'tail':
                self.add_tail(node)
            else:
                raise ValueError('Wrong construct mode, only support "head" and "tail"!')

    def add_head(self, node):
        n = self.head.next
        n.prev, self.head.next = node, node
        node.prev, node.next = self.head, n
        self.length += 1

    def add_tail(self, node):
        p = self.tail.prev
        p.next, self.tail.prev = node, node
        node.prev, node.next = p, self.tail
        self.length += 1

    def remove_head(self):
        if self.head.next is not self.tail:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.length -= 1

    def remove_tail(self):
        if self.tail.prev is not self.head:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.length -= 1

    def traverse(self):
        node = self.head.next
        while node is not self.tail:
            print(node.val)
            node = node.next


if __name__ == '__main__':
    dll = DoublyLinkedList([1, 2, 3, 4], 'head')

    dll.remove_head()
    dll.traverse()
    print('length: ', dll.length)

    dll.remove_tail()
    dll.remove_tail()
    dll.traverse()
    print('length: ', dll.length)
