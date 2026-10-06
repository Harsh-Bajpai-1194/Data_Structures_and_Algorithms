class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = c1 = 0
        for i in s:
            if i == "(": c += 1
            else:
                if c > 0: c -= 1
                else: c1 += 1
        return c1 + c