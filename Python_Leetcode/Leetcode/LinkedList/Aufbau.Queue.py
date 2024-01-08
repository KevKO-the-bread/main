
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = self.tail = None
        
    def enqueue(self, val):
        newNode = ListNode(val)
        
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode
    
    def dequeue(self):
        if not self.head:
            return None
        else:
            temp = self.head.val
            self.head = self.head.next
            return temp
    
    def print_queue(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
