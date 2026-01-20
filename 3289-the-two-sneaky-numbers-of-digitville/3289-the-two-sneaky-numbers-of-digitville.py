class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in nums:
            if nums.count(i)==2 and i not in L: L.append(i)
        L.sort()
        return L