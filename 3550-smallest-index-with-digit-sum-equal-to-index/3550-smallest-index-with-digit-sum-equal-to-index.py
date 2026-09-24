class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum=0
            while(nums[i]!=0):
                sum+=nums[i]%10
                nums[i]//=10
            if i==sum:
                return i
        return -1