class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in set(s):
            start = s.find(c)
            end = s.rfind(c)
            if start < end:
                res += len(set(s[start + 1 : end]))
        return res