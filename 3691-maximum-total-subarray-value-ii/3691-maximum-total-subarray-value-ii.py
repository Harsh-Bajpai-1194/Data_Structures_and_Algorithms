class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        n, b = len(nums), len(nums).bit_length()
        M, m = [[x] * b for x in nums], [[x] * b for x in nums]
        for j in range(1, b):
            for i in range(n - (1 << j) + 1):
                M[i][j], m[i][j] = max(M[i][j - 1], M[i + (1 << (j - 1))][j - 1]), min(m[i][j - 1], m[i + (1 << (j - 1))][j - 1])
        def q(l, r):
            j = (r - l + 1).bit_length() - 1
            return max(M[l][j], M[r - (1 << j) + 1][j]) - min(m[l][j], m[r - (1 << j) + 1][j])
        pq = [(-q(l, n - 1), l, n - 1) for l in range(n)]; heapq.heapify(pq); ans = 0
        for i in range(k):
            v, l, r = heapq.heappop(pq); ans -= v
            if r > l: heapq.heappush(pq, (-q(l, r - 1), l, r - 1))
        return ans