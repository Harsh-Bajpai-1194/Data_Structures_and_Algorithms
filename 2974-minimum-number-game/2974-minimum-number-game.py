class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        alice=0
        bob=0
        arr=[]
        for i in range(len(nums)//2):
            alice=min(nums)
            nums.remove(min(nums))
            bob=min(nums)
            nums.remove(min(nums))
            arr.append(bob)
            arr.append(alice)
            alice=0
            bob=0
        return arr