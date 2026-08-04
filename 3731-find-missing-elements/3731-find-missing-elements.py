class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        L=[]
        for i in range(min(nums),max(nums)):
            if i not in nums: 
                L.append(i)
        return sorted(L)