class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        s="".join(letters).replace(target,"")
        if s[0]>target: return s[0]
        for i in s:
            if i>target: return i
        return s[0]