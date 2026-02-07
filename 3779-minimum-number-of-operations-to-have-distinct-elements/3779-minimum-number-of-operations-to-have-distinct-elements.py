class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=-1
        L=set()
        i=len(nums)-1
        while(i>-1):
            if nums[i] in L:
                j=i
                break
            L.add(nums[i])
            i-=1
        if j==-1: return 0
        return j//3+1