class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        A=nums
        A.sort()        
        return max(A[-1] * A[-2] * A[-3],A[-1] * A[0] * A[1])