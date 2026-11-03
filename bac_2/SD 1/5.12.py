class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return f"({self.left}{self.value}{self.right})"

    def print_tree(self, niveau=0):
        if self.right is not None:
            self.right.print_tree(niveau + 1)

        print(" " * (2 * niveau) + str(self.value))

        if self.left is not None:
            self.left.print_tree(niveau + 1)

test_tree = Node('+', Node('3'), Node('*', Node('2'), Node('5')))
test_tree.print_tree()