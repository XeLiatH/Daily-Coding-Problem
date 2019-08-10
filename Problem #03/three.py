# -*- coding: utf8 -*-


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val


def serialize(root: Node):
    if root is None:
        return '-'
    return root.val + '-' + serialize(root.left) + serialize(root.right)


def deserialize(s: str):
    nodes = s.split('-')
    return deserializeNode(nodes)


def deserializeNode(nodes: list):
    if len(nodes) < 1:
        return None

    node = nodes.pop(0)  # pops from the start of the list
    if node is None:
        return None

    node = Node(node)
    node.left = deserializeNode(nodes)
    node.right = deserializeNode(nodes)
    return node


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
