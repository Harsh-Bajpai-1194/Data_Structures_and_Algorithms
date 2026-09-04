class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums)==0: return -1
        L=[0]*len(nums)
        L[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            L[i]=min(L[i+1],nums[i])
        maximum=float('-inf')
        for i in range(len(nums)):
            maximum=max(maximum,nums[i])
            if maximum-L[i]<=k: return i
        return -1