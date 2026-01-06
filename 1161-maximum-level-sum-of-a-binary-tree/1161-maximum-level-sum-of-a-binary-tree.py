# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        from collections import deque
        queue = deque([root])
        max_sum = float('-inf')
        max_level = 0
        level = 0
        while queue:
            level += 1
            level_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
        return max_level