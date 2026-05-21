class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        L=set()
        c=0
        for i in arr1:
            while i>0:
                L.add(i)
                i=i//10
        for i in arr2:
            while i>0:
                if i in L:
                    c=max(c,len(str(i)))
                    break
                i=i//10
        return c     