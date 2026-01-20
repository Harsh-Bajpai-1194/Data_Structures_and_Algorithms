# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_to_delete = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val in nums_to_delete: prev.next = curr.next
            else: prev = curr
            curr = curr.next
        return dummy.next