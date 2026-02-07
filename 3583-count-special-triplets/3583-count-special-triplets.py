class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        MOD = 10**9 + 7
        right_counts = Counter(nums)
        left_counts = Counter()
        total_triplets = 0
        for num in nums:
            right_counts[num] -= 1
            target = num * 2
            if left_counts[target] > 0 and right_counts[target] > 0:
                count = (left_counts[target] * right_counts[target])
                total_triplets = (total_triplets + count) % MOD
            left_counts[num] += 1
        return total_triplets