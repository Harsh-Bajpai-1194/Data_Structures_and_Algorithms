class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        count = s.count('0')
        result = count
        val = 0
        power = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if power > k:
                    break
                val += power
                if val > k:
                    break
                result += 1
            power <<= 1
        return result