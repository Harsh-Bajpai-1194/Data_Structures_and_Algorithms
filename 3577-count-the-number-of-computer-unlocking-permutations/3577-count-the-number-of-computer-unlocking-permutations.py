class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        n = len(complexity)
        if n <= 1: return 1
        root_complexity = complexity[0]
        MOD = 10**9 + 7
        for i in range(1, n):
            if complexity[i] <= root_complexity: return 0
        ans = 1
        for i in range(1, n): ans = (ans * i) % MOD
        return ans