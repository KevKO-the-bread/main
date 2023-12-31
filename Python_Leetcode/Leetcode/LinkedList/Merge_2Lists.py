class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def iterate(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next


# Beispielanwendung
list1 = LinkedList()
list1.add(1)
list1.add(3)
list1.add(5)

list2 = LinkedList()
list2.add(2)
list2.add(4)
list2.add(6)

linked_list = LinkedList()
merged_list = linked_list.merge_two_lists(list1.head, list2.head)

linked_list.head = merged_list

linked_list.iterate()

#without second list ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def iterate(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None or list2 is None:
            return list1 or list2

        merged_list = None
        curr = None

        while list1 and list2:
            if list1.val <= list2.val:
                new_node = ListNode(list1.val)
                if merged_list is None:
                    merged_list = new_node
                    curr = merged_list
                else:
                    curr.next = new_node
                    curr = curr.next
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                if merged_list is None:
                    merged_list = new_node
                    curr = merged_list
                else:
                    curr.next = new_node
                    curr = curr.next
                list2 = list2.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return merged_list

# Example usage
list1 = LinkedList()
list1.add(1)
list1.add(3)
list1.add(5)

list2 = LinkedList()
list2.add(2)
list2.add(4)
list2.add(6)


merged_list = list1.merge_two_lists(list1.head, list2.head)

# Create a new instance of LinkedList using merged_list
merged_list_instance = LinkedList()
merged_list_instance.head = merged_list

# Call iterate on the new instance
merged_list_instance.iterate()
