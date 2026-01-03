class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        max=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                if max<count:
                    max=count
                count=0
        return max