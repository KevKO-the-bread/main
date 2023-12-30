
class LinkedList:
  def remove_last_element(self):
        if self.head is None:
            return

        curr = self.head
        while curr.next.next:
            curr = curr.next

        curr.next = None
        self.tail = curr


    def remove_first_element(self):
        if self.head is None:
            return
        temp=self.head
        self.head=self.head.next
        temp= None
        
        
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
