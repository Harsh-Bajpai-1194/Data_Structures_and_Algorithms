class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or str(x)!=str(x)[-1::-1]: return False
        return True