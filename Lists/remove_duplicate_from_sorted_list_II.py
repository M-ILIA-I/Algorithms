# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Problem description:

    Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list. Return the linked list sorted as well.

    Examples:

    Input: head = [1,1,1,2,3]
    Output: [2,3]
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        flag = 1
        while head.next:
            if head.val == head.next.val:
                flag = 0
                head = head.next
                if not head.next:
                    return None
            elif head.val != head.next.val:
                if flag:
                    break
                head = head.next
                flag = 1
        
        ptr = head
        prev_ptr = head

        flag = 0 
        while ptr.next:
            if ptr.val == ptr.next.val:
                flag = 1
                ptr = ptr.next
                if not ptr.next:
                    prev_ptr.next = None
                    break
            elif ptr.val != ptr.next.val:
                if flag:
                    flag = 0
                    ptr = ptr.next
                    prev_ptr.next = ptr
                    continue
                    
                prev_ptr = ptr
                ptr = ptr.next
                
        return head