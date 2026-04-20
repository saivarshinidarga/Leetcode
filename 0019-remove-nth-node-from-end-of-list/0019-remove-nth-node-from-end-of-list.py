# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        # Step 1: move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Step 2: move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Step 3: delete the nth node from end
        slow.next = slow.next.next

        return dummy.next
