class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        L=list(ransomNote)
        L1=list(magazine)
        for i in L:
            if i in L1: L1.remove(i)
            else: return False
        return True