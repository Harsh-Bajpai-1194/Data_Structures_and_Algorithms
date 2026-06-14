# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = fast = head
        previous = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, previous, slow = previous, slow, slow.next
        result = 0
        while slow:
            result = max(result, previous.val + slow.val)
            previous, slow = previous.next, slow.next
        return result