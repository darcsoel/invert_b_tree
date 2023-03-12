"""
Unit tests
"""

from main import Node


def test_1() -> None:
    node = Node(5)
    node.insert(2)
    node.insert(1)
    node.insert(3)
    node.insert(7)
    node.insert(6)
    node.insert(8)

    assert node.left.value == 2
    assert node.left.left.value == 1
    assert node.left.right.value == 3

    assert node.right.value == 7
    assert node.right.left.value == 6
    assert node.right.right.value == 8

    inverted = node.invert()

    assert inverted.value == 5
    assert inverted.left.value == 7
    assert inverted.left.left.value == 8
    assert inverted.left.right.value == 6
