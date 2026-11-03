
def operator(c):
    if c == '+':
        return lambda x, y: x + y
    elif c == '-':
        return lambda x, y: x - y
    elif c == '*':
        return lambda x, y: x * y
    elif c == '/':
        return lambda x, y: x / y

def calc(tree):
    if tree.left is None and tree.right is None:
        return float(tree.value)
    else:
        return operator(tree.value)(calc(tree.left), calc(tree.right))

Node = lambda value, left=None, right=None: type('Node', (object,), {'value': value, 'left': left, 'right': right})()
tree = Node('+', Node('3'), Node('*', Node('2'), Node('5')))
print(calc(tree))
