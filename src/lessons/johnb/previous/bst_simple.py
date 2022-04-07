from random import randrange


class TreapNode:
    def __init__(self, data, priority=100, left=None, right=None):
        self.data = data
        self.priority = randrange(priority)
        self.left = left
        self.right = right


''' Function to left-rotate a given treap

	  r                       r
	 / \     Left Rotate     / \
	l   r       ———>        r   y
	   / \                     / \
	  x   y                   l   x
'''


def rotate_left(root):
    r = root.right
    x = root.right.left

    r.left = root
    root.right = x

    return r


''' Function to right-rotate a given treap

		r                        l
	   / \     Right Rotate     / \
	  l   r       ———>         x   r
	 / \                          / \
	x   y                        y   r
'''


def rotate_right(root):
    l = root.left
    y = root.left.right

    l.right = root
    root.left = y

    return l


def insert_node(root, data):
    if root is None:
        return TreapNode(data)
    if data < root.data:
        root.left = insert_node(root.left, data)
        if root.left and root.left.priority > root.priority:
            root = rotate_right(root)
    else:
        root.right = insert_node(root.right, data)
        if root.right and root.right.priority > root.priority:
            root = rotate_left(root)
    return root


def search_node(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search_node(root.left, key)
    return search_node(root.right, key)


def delete_node(root, key):
    if root is None:
        return None
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None and root.right is None:
            root = None
        elif root.left and root.right:
            if root.left.priority < root.right.priority:
                root = rotate_left(root)
                root.left = delete_node(root.left, key)
            else:
                root = rotate_right(root)
                root.right = delete_node(root.right, key)
        else:
            child = root.left if (root.left) else root.right
            root = child
    return root


def print_treap(root, space):
    height = 10
    if root is None:
        return
    space += height
    print_treap(root.right, space)
    for i in range(height, space):
        print(' ', end='')
    print((root.data, root.priority))
    print_treap(root.left, space)


if __name__ == '__main__':
    keys = [5, 2, 1, 4, 9, 8, 10]
    root = None
    for key in keys:
        root = insert_node(root, key)
    print("Inserted :\n\n")
    print_treap(root, 0)
    print("\nDeleted 1:\n\n")
    root = delete_node(root, 1)
    print_treap(root, 0)
    print("\nDeleted 5:\n\n")
    root = delete_node(root, 5)
    print_treap(root, 0)
    print("\nDeleted 9:\n\n")
    root = delete_node(root, 9)
    print_treap(root, 0)
