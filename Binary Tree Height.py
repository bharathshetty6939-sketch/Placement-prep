class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
def get_height(node):
    if node is None:
        return 0
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return 1 + max(left_height, right_height)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

print("The height of the tree is:", get_height(root))