class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def iterate(self):

        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next


listofnodes = LinkedList()
listofnodes.head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(4)
listofnodes.head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# current.next = nextdist

# nextdist


def removeduplicates(linkedlist):
    prevnode = linkedlist.head
    currentnode = linkedlist.head.next
    while currentnode is not None:
        if prevnode.val == currentnode.val:
            currentnode = currentnode.next
        elif prevnode.val != currentnode.val:
            prevnode.next = currentnode
            prevnode = currentnode

    if currentnode is None:
        prevnode.next = currentnode

    return linkedlist


"""
1 = prevnode
2 = prevnode.next / currentnode
3 =
4 =
4 =
none = 
"""

removeduplicates(listofnodes)
listofnodes.iterate()
