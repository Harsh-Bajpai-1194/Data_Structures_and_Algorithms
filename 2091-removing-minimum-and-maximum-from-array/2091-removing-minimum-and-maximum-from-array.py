class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        for i in range(1, n):
            if nums[i] < nums[l]: l = i
            if nums[i] > nums[r]:r = i         
        if l < r:
            l, r = r, l
        ans = n
        for i in range(n + 1):
            c = 0
            if r >= i: c = n - r
            elif l >= i: c = n - l
            ans = min(ans, i + c)
        return ans