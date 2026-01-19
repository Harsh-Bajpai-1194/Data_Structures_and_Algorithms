class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        c=0
        for i in words:
            if i[:len(pref)]==pref: c+=1
        return c