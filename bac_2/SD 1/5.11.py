class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return f"({self.left}{self.value}{self.right})"


test_tree = Node('+', Node('3'), Node('*', Node('2'), Node('5')))
print(test_tree)