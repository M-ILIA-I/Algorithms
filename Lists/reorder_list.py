# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Description problem:

        You are given the head of a singly linked-list. The list can be represented as:

        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
        """
        if not head.next or not head.next.next:
            return head

        slow = head
        fast = head

        while True:
            while fast.next.next:
                fast = fast.next
            
            fast.next.next = slow.next
            slow.next = fast.next
            slow = fast.next.next
            fast.next = None
            fast = slow
            if not slow.next or not slow.next.next:
                return head
        
            
        