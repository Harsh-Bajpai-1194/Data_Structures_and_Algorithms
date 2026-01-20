class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        s1=""
        for i in words: s1+=i[0]
        return s==s1
