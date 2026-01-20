class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
            for j in range(0,max(nums)):
                if j|(j+1)==i: 
                    ans.append(j)
                    break
            else: ans.append(-1)
        return ans