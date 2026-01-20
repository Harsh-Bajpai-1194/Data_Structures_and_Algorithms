class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        ans = float('inf')
        total = sum(freq)
        for i in range(n):
            max_allowed = freq[i] + k
            deletions = 0
            for j in range(n):
                if freq[j] > max_allowed:
                    deletions += freq[j] - max_allowed
            deletions += sum(freq[:i])
            ans = min(ans, deletions)
        return ans