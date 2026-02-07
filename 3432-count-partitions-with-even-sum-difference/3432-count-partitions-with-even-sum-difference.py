class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(1,len(nums)):
            left_sum=sum(nums[:i])
            right_sum=sum(nums)-left_sum
            if left_sum%2==right_sum%2: c+=1
        return c