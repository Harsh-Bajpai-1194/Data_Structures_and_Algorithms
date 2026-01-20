class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        L=[words[0]]
        for i in range(1,len(words)):
            if "".join(sorted(words[i]))!="".join(sorted(words[i-1])):
                L.append(words[i])
        return L