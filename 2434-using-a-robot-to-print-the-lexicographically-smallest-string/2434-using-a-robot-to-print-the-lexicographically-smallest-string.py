class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        freq = Counter(s)
        t = []
        res = []
        min_char = 'a'
        for c in s:
            t.append(c)
            freq[c] -= 1
            while min_char <= 'z' and freq[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            while t and t[-1] <= min_char:
                res.append(t.pop())
        return ''.join(res)