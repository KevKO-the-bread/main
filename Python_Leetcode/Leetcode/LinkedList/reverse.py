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


    def iterate(self):
        curr = self.tail
        while curr:
            val = curr.data
            yield val
            curr = curr.next


def main():
    items = LinkedList()
    items.add(1)
    items.add(2)
    items.add(3)

    items.reverse()

    for i in items.iterate():
        print(i)

if __name__ == "__main__":
    main()
