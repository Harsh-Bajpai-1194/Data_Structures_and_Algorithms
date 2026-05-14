class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        if nums.count(max(nums))!=2 or n!=max(nums)+1: 
            return False
        nums.sort()
        for i in range(1,n-1):
            if nums[i]-nums[i-1]!=1:
                return False
        return True