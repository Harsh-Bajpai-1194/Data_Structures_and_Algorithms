class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min=nums[0]
        max=nums[0]
        for i in range(len(nums)):
            if (nums[i]<min): min=nums[i]
            elif (nums[i]>max): max=nums[i]
        num1=min
        num2=max
        while(num1>0):
            temp=num2%num1
            num2=num1
            num1=temp
        return num2