class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in s:
            if i in "aeiou": return True
        return False