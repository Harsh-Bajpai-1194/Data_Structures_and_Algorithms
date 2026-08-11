class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A=nums
        n = len(A)
        L = set(A)
        sum = A[0]
        for i in range(1, n):
            if A[i] == A[i - 1] + 1: sum += A[i]
            else: break
        while sum in L:
            sum += 1
        return sum