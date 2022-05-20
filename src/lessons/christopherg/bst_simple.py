"""
        10
       /  \
      5   20
     /   /  \
    4   22   39

"""


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root


def search(root, value):
    if root is None:
        return False
    elif root.data == value:
        return True
    elif root.data > value:
        return search(root.leftChild, value)
    else:
        return search(root.rightChild, value)


root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)
print("53 is present in the binary tree:", search(root, 53))
print("100 is present in the binary tree:", search(root, 100))
