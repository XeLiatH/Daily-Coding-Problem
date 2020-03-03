# -*- coding: utf-8 -*-

"""
    > 006 @ Google
    ~~~~~~~~~~~~~~
    An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding
    ```next``` and ```prev``` fields, it holds a field named ```both```, which is an XOR of the next
    node and the previous node. Implement an XOR linked list; it has an ```add(element)``` which adds
    the element to the end, and a ```get(index)``` which returns the node at index.

    If using a language that has no pointers (such as Python), you can assume you have access
    to ```get_pointer``` and ```dereference_pointer``` functions that converts between
    nodes and memory addresses.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.both = id(data)


class LinkedList:
    # property ids simulates object pointers
    def __init__(self, node: Node, ids: dict):
        self.head = node
        self.tail = node
        self.head.both = 0
        self.tail.both = 0
        self.ids = ids

    def add(self, element: Node):
        self.tail.both ^= id(element.data)
        element.both = id(self.tail.data)
        self.tail = element

    def get(self, index):
        prev_node_address = 0
        result_node = self.head
        for i in range(index):
            next_node_address = prev_node_address ^ result_node.both
            prev_node_address = id(result_node.data)
            result_node = self.ids[next_node_address]

        return result_node.data


if __name__ == '__main__':
    node_1 = Node('1')
    node_2 = Node('2')
    node_3 = Node('3')
    node_4 = Node('4')

    pointer_map = dict()
    pointer_map[id('1')] = node_1
    pointer_map[id('2')] = node_2
    pointer_map[id('3')] = node_3
    pointer_map[id('4')] = node_4

    linked_list = LinkedList(node_3, pointer_map)
    linked_list.add(node_2)
    linked_list.add(node_4)
    linked_list.add(node_1)

    assert linked_list.get(0) == '3'
    assert linked_list.get(1) == '2'
    assert linked_list.get(2) == '4'
    assert linked_list.get(3) == '1'
