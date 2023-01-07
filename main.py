from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    def insert(self, value: int) -> None:
        """Insert new node"""

        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)


def invert(node: Node) -> Node:
    node.left, node.right = node.right, node.left

    if node.left:
        invert(node.left)

    if node.right:
        invert(node.right)

    return node
