class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        ans = target[0]
        for a, b in zip(target, target[1:]):
            if a < b:
                ans += b-a
        return ans  