class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class singly_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data):
        new_node = node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail=new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.count += 1

    def iterate_item(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next


items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
for val in items.iterate_item():
    print(val)
print("\nhead.data: ", items.head.data)
print("tail.data: ", items.tail.data)
