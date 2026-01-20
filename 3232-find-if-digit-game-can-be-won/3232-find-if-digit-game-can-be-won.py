class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        alice,bob=[],[]
        for i in nums:
            if i<10:
                alice.append(i)
            else:
                bob.append(i)
        if sum(alice)==sum(bob): return False
        return True