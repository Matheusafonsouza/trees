from __future__ import annotations


class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self) -> str:
        return self.data


class BinaryTree:
    def __init__(self) -> None:
        self.head = None

    def __print_tree(self, node: Node):
        if not node:
            return None

        print(f"{node.data} -> ", end=" ")
        self.__print_tree(node.left)
        self.__print_tree(node.right)

    def print_tree(self) -> None:
        node = self.head
        self.__print_tree(self.head)
        while node != None:
            node = node.left or node.right


if __name__ == "__main__":
    tree = BinaryTree()

    node_a = Node(data="a")
    node_b = Node(data="b")
    node_c = Node(data="c")
    node_d = Node(data="d")
    node_e = Node(data="e")
    node_f = Node(data="f")

    node_a.left = node_b
    node_a.right = node_d
    node_b.left = node_c
    node_d.left = node_e
    node_d.right = node_f

    tree.head = node_a
    tree.print_tree()
