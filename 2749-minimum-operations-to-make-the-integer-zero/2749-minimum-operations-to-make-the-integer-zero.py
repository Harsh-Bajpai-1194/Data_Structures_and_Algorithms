class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in range(1, 61):
            target = num1 - num2 * k
            if target < k:
                continue
            if bin(target).count("1") <= k <= target:
                return k
        return -1