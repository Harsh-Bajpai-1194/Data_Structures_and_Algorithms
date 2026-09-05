class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums)==0: return -1
        L=[0]*len(nums)
        L[0]=nums[0]
        for i in range(1,len(nums)):
            L[i]=max(L[i-1],nums[i])
        L1=[0]*len(nums)
        L1[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            L1[i]=min(nums[i],L1[i+1])
        for i in range(len(nums)):
            a=L[i]-L1[i]
            if a<=k: return i
        return -1