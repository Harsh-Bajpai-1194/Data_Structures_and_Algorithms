class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        L=[i**2 for i in nums]
        n=len(nums)//2
        L.sort()
        for i in range(n): L[i]*=-1
        return sum(L)