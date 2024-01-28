class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findMinValue(node):
    current = node

    # переходимо до крайнього лівого вузла
    while current.left is not None:
        current = current.left

    return current.val

# Функція для додавання елемента в BST (використовується для демонстрації)
def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.val:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

# Демонстрація використання
root = None
values = [15, 10, 20, 8, 12, 16, 25]  # Приклад значень для додавання в дерево
for value in values:
    root = insert(root, value)

print("Найменше значення в дереві:", findMinValue(root))
