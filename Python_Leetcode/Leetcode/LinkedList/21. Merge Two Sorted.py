class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    if list1:
        node.next = list1

    if list2:
        node.next = list2

    return dummy.next


merged_list = mergeTwoLists(list1, list2)

while merged_list:
    print(merged_list.val)
    merged_list = merged_list.next

    
