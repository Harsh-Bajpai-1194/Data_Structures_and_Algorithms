# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        all_sums = []
        def get_subtree_sum(node):
            if not node: return 0
            left_sum = get_subtree_sum(node.left)
            right_sum = get_subtree_sum(node.right)
            current_sum = node.val + left_sum + right_sum
            all_sums.append(current_sum)
            return current_sum
        total_sum = get_subtree_sum(root)
        max_prod = 0
        for s in all_sums:
            current_prod = s * (total_sum - s)
            max_prod = max(max_prod, current_prod)
        return max_prod%(10**9+7)