url= https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):

        if not head:
            return head



        tail=head
        count=1

        while tail.next:
            tail=tail.next
            count+=1

        curr=head

        k=k%count
        if k ==0:
            return head

        for i in range (count-1-k):
            curr=curr.next

        solution=curr.next
        curr.next=None
        tail.next=head

        return solution
