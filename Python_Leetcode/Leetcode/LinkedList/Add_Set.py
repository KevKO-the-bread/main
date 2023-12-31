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
        
   

    def iterate(self):
        curr = self.head
        while curr:
            val = curr.data
            yield val
            curr = curr.next
            
    def add_start(self, value):
        if self.head is None:
            new_node=Node(value)
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(value)
            temp=self.head
            self.head=new_node
            self.head.next=temp
            
    def add_anywhere(self, value,n):
            if n==0:
                self.add_start(value)
                return
        
            new_Node=Node(value)
            curr=self.head
            prev=None
            while n>0:
                prev=curr
                curr=curr.next
                n-=1
                if curr is None and n>0:
                    return
            
            if curr is None:
                self.add(value)
                return

            prev.next=new_Node
            prev.next.next= curr
            
    def set_item(self, value, replace):
        curr=self.head 
        while curr.data!= replace:
            curr=curr.next
        curr.data= value
    
        
            
        
            
        


def main():
    items = LinkedList()
    items.add(1)
    items.add(2)
    items.add(3)
    items.add_start(4)
    items.add_anywhere(10, 4)
    items.set_item("aws", 3)
    
   
   
    
    
    
    

    for i in items.iterate():
        print(i)

if __name__ == "__main__":
    main()
