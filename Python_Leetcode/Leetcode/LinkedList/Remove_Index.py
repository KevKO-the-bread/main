class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next  # Save reference to next node
            curr.next = prev  # Reverse current node's pointer
            prev = curr  # Update previous node
            curr = temp  # Update current node
        temp=self.head 
        self.head= self.tail 
        self.tail= temp
        
    def remove_last_element(self):
        if self.head is None:
            return
        curr = self.head
        
        if curr.next is None:
            self.head=self.head.next
            curr=None
            return

        while curr.next.next:
            curr = curr.next

        curr.next = None
        self.tail = curr


    def remove_first_element(self):
        if self.head is None:
            return
        self.head=self.head.next
        
    def remove_any_element(self, value):
        if self.head is None:
            return
        curr=self.head 
        prev=None
        
        while curr.data!= value:
            prev=curr 
            curr=curr.next    
        prev.next=curr.next 
        curr= None


    def iterate(self):
        curr = self.head
        while curr:
            val = curr.data
            yield val
            curr = curr.next


def main():
    items = LinkedList()
    items.add(1)
    items.add(2)
    items.add(3)
    
    items.remove_any_element(2)
    items.remove_last_element()
    items.remove_first_element()
    
    
    
    

    for i in items.iterate():
        print(i)

if __name__ == "__main__":
    main()
