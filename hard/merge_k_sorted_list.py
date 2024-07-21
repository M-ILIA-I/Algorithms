# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Problem description 

    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hm = {}

        for i in range(len(lists)):
            while lists[i]:
                if lists[i].val in hm:
                    hm[lists[i].val] += 1
                else:
                    hm[lists[i].val] = 1
                lists[i] = lists[i].next

        sorted_hm = sorted(hm.items(), key=lambda x: x[0])
        head = ListNode()
        dummy = head

        for i in range(len(sorted_hm)):
            j = 0
            while j != sorted_hm[i][1]:
                dummy.next = ListNode(sorted_hm[i][0])
                dummy = dummy.next
                j += 1
        return head.next
    