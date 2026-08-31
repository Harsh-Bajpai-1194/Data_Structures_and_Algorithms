# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], maxi = float('inf'), mini = float('-inf')) -> bool:
        if root is None:
            return True
        return root.val < maxi and root.val > mini and self.isValidBST(root.left, root.val, mini) and self.isValidBST(root.right, maxi, root.val)