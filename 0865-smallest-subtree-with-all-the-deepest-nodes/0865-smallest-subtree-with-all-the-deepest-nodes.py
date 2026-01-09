# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def helper(node):
            if not node: return 0, None
            left_depth, left_subtree = helper(node.left)
            right_depth, right_subtree = helper(node.right)
            if left_depth == right_depth: return left_depth + 1, node
            if left_depth > right_depth: return left_depth + 1, left_subtree
            else: return right_depth + 1, right_subtree
        return helper(root)[1]