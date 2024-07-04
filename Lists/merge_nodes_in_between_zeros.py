# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem description:

        You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

        For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

        Return the head of the modified linked list.
        """
        while head.val == 0:
            head = head.next

        tmp_sum = 0
        tmp_node = head
        res_head = head

        while tmp_node:
            if tmp_node.val == 0:
                head.val = tmp_sum
                head.next = tmp_node.next
                head = tmp_node.next
                tmp_node = tmp_node.next
                tmp_sum = 0
            else:
                tmp_sum += tmp_node.val
                tmp_node = tmp_node.next

        return res_head