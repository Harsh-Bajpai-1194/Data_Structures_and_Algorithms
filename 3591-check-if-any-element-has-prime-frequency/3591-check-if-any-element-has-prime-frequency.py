class Solution(object):
    def prime(self, n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        frequency=[0]*101
        for num in nums:
            frequency[num] += 1
        for count in frequency:
            if self.prime(count):
                return True
        return False