url=https://leetcode.com/problems/reverse-linked-list-ii/description/

class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy=ListNode(0, head) #dummyNode

        prev=dummy
        curr=head
      
        for i in range(left-1):   #reach position for l
            prev=curr
            curr=curr.next
        l=curr
        l_prev=prev
        
        diff=right-left+1
        
        for i in range (diff):    #reverse
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        l_prev.next=prev    #Node Anfang
        l.next=temp         #Node Ende
        
        return dummy.next
