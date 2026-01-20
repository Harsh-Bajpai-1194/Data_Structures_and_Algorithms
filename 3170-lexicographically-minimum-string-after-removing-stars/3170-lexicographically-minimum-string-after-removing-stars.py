class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = list(s)
        buckets = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == '*':
                ans[i] = ''
                j = next(j for j, bucket in enumerate(buckets) if bucket)
                ans[buckets[j].pop()] = ''
            else:
                buckets[ord(c) - ord('a')].append(i)
        return ''.join(ans)