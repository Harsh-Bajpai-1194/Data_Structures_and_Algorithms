class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            n=len(nums)
            s=sum(nums)
            total=0
            for i in range(n):
                total+=i*nums[i]
            maximum=total
            for i in range(n-1,-1,-1):
                total+=s-n*nums[i]
                maximum=max(maximum,total)
        return maximum