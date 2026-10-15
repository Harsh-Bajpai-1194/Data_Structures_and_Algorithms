class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        for i in range(n):
            s=set()
            for j in range(i, n):
                s.add(nums[j])
                sum+=len(s)**2
        return sum