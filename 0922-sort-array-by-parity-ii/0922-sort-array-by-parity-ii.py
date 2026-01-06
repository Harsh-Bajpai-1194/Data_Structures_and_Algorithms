class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==1: return nums
        odd=[]
        even=[]
        for i in nums:
            if i%2==0: even.append(i)
            else: odd.append(i)
        even.sort(reverse=True)
        odd.sort()
        nums=[0]*len(nums)
        for i in range(0,len(nums),2): nums[i]=even[i//2]
        for i in range(1,len(nums),2): nums[i]=odd[i//2]
        return nums