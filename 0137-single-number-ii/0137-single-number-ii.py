class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]: 
            return nums[0]
        if (n-1)%3==0 and nums[-1]!=nums[-2]: 
            return nums[-1]
        for i in range(3, n, 3):
            if nums[i]!=nums[i+1]:
                return nums[i]