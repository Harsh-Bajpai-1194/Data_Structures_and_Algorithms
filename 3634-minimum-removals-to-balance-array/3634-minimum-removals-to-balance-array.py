class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        i,j,maximum=0,0,0
        nums.sort()
        for j in range(len(nums)):
            if (nums[j]>nums[i]*k): i+=1
            window=j-i+1
            maximum=max(maximum,window)
        return len(nums)-maximum