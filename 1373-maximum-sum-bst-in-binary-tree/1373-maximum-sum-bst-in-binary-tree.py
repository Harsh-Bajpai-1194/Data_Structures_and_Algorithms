# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = 0
        def rec(node):
            if not node:
                return True, 0, float('inf'), float('-inf')
            left_is_bst, left_sum, left_min, left_max = rec(node.left)
            right_is_bst, right_sum, right_min, right_max = rec(node.right)
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_sum = node.val + left_sum + right_sum
                self.res = max(self.res, current_sum)
                return True, current_sum, min(node.val, left_min), max(node.val, right_max)
            return False, 0, 0, 0
        rec(root)
        return self.res