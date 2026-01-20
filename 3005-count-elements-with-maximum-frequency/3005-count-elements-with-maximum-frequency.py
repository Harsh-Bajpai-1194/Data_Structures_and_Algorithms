class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count,L=0,[]
        for i in nums:
            if nums.count(i)>=count:
                count=nums.count(i)
        for i in nums:
            if nums.count(i)==count: L.append(i)
        return count*len(set(L))