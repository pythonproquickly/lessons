class BSTNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def levelOrder(root):
    q = []
    q.append(root)
    q.append(None)

    while True:
        currentNode = q.pop(0)
        if currentNode is not None:
            print(currentNode.val, end=' ')
            if currentNode.left is not None:
                q.append(currentNode.left)
            if currentNode.right is not None:
                q.append(currentNode.right)
        else:
            print()
            if len(q) == 0:
                break
            q.append(None)


vals = [10, 11, 2]
root = BSTNode(10)
root.left = BSTNode(2)
root.right = BSTNode(11)
levelOrder(root)

'''
 10
/  \
2  11
'''
