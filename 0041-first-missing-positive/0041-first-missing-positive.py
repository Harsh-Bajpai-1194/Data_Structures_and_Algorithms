class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        L=[]
        for i in nums:
            if i>0:
                L.append(i)
        L=list(set(L))
        L.sort()
        if L==[] or L[0]!=1:
            return 1
        for i in range(1,len(L)):
            if L[i]!=i+1:
                return i+1
        return len(L)+1