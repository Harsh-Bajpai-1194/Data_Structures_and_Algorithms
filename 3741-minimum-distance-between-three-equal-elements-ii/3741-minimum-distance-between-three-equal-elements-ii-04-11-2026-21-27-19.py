class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        L = [-1] * len(nums)
        L1 = {}
        ans = len(nums) + 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in L1:
                L[i] = L1[nums[i]]
            L1[nums[i]] = i
        for i in range(len(nums)):
            a = L[i]
            if a != -1:
                b = L[a]
                if b != -1:
                    ans = min(ans, b - i)
        return -1 if ans==len(nums)+1 else ans*2