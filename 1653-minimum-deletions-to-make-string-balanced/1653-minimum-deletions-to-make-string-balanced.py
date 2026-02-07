class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count_a,count_b=[0]*n,[0]*n
        b_count = 0
        for i in range(n):
            count_b[i] = b_count
            if s[i] == "b": b_count += 1
        a_count = 0
        for i in range(n - 1, -1, -1):
            count_a[i] = a_count
            if s[i] == "a": a_count += 1
        min_deletions = n
        for i in range(n): min_deletions = min(min_deletions, count_a[i] + count_b[i])
        return min_deletions