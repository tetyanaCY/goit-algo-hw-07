class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sumOfValues(node):
    if node is None:
        return 0

    return node.val + sumOfValues(node.left) + sumOfValues(node.right)

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

print("Сума всіх значень в дереві:", sumOfValues(root))
