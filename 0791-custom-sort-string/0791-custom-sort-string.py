class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        from collections import Counter
        count=Counter(s)
        L=[]
        for char in order:
            if char in count:
                L.append(char*count[char])
                del count[char] 
        for char in count:
            L.append(char*count[char])
        return ''.join(L)