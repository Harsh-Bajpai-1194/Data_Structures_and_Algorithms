class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L=list(set(nums))
        sum=0
        for i in L:
            if nums.count(i)%k==0:
                sum=sum+i*nums.count(i)
        return sum