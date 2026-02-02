class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(words)-1):
            if words[i][-1::-1] in words[i+1:len(words)]: c+=1
        return c