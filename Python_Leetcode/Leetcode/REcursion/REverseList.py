url=https://leetcode.com/problems/reverse-linked-list/description/


# Recursive implementation of n! (n-factorial) calculation
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)
class Solution:
    def reversedList(self, head)

    if not head:
        return head
    newNead=head
    if head.next:
        newHead=self.reverseList(head.next)
        head.next.next=head
    head.next=None
