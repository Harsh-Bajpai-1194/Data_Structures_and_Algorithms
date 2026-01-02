class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        L=[]
        for i, word in enumerate(words):
            if x in word:
                L.append(i)
        return L