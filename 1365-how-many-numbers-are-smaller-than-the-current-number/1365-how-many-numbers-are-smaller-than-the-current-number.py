class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        L=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j]<nums[i]: count+=1
            L.append(count)
        return L