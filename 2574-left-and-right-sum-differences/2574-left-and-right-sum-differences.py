class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        L.append(0)
        for i in range(len(nums)): L.append(L[i]+nums[i])
        nums.reverse()
        for i in range(1,len(nums)): nums[i]+=nums[i-1]
        nums.pop(-1)
        nums.insert(0,0)
        nums.reverse()
        L.pop(-1)
        for i in range(len(nums)): nums[i]=abs(nums[i]-L[i])
        return nums