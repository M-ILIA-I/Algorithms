# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Given the head of a linked list, remove the nth node from the end of the list and return its head."""
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            dummy = dummy.next
            head = head.next

        dummy.next = dummy.next.next

        return res.next