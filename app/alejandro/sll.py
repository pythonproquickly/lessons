class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


def insertValueIntoSortedLinkedList(l, value):
    thisNode = l
    while True:
        if thisNode.value > value:
            next_node = ListNode(thisNode.value)
            next_node.next = thisNode.next
            thisNode.value = value
            thisNode.next = next_node
            return
        if thisNode.next is None:
            break
        thisNode = thisNode.next
    thisNode.next = ListNode(value)


l = ListNode(1)
insertValueIntoSortedLinkedList(l, 9)
insertValueIntoSortedLinkedList(l, 8)
insertValueIntoSortedLinkedList(l, 1)
insertValueIntoSortedLinkedList(l, 22)
insertValueIntoSortedLinkedList(l, -9)

while l is not None:
    print(l.value)
    l = l.next
