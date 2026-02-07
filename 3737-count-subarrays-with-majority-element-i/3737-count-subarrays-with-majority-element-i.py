class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dresaniel = nums
        n = len(nums)
        offset = n + 1
        bit_size = 2 * n + 2
        bit = [0] * (bit_size + 1)
        def update(i, delta):
            while i < len(bit):
                bit[i] += delta
                i += i & (-i)
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        prefix_sum = 0
        count = 0
        update(0 + offset, 1)
        for num in nums:
            if num == target: prefix_sum += 1
            else: prefix_sum -= 1
            count += query(prefix_sum + offset - 1)
            update(prefix_sum + offset, 1)
        return count