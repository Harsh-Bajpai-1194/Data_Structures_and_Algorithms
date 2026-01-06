class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        res = -1
        for num, count in freq.items():
            if num == count:
                res = max(res, num)
        return res