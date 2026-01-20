class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        m = len(potions)
        res = []
        for spell in spells:
            target = (success + spell - 1) // spell 
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] < target: l = mid + 1
                else: r = mid - 1
            res.append(m - l)
        return res