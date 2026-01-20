class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L,L1=[],[]
        for i in range(len(nums)):
            if bin(i)[2:].count("1")==k: 
                L.append(bin(i)[2:])
                L1.append(i)
        sum=0
        for i in L1: sum+=nums[i]
        return sum