url=https://leetcode.com/problems/design-linked-list/description/

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.right = ListNode(0)
        self.left = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val):
        prev, next, node = self.left, self.left.next, ListNode(val)
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def addAtTail(self, val):
        prev, next, node = self.right.prev, self.right, ListNode(val)
        next.prev = node
        prev.next = node
        node.prev = prev
        node.next = next

    def addAtIndex(self, index, val):
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0:
            next = curr
            prev = curr.prev
            node = ListNode(val)
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index):
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0 and curr!=self.right:
            prev = curr.prev
            next = curr.next
            prev.next = next
            next.prev = prev
