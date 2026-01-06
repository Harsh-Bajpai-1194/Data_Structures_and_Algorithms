class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in range(0,len(nums),2): L+=[nums[i+1]]*nums[i]
        return L