class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[None,None]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    L[0]=i
                    L[1]=j
                    return L