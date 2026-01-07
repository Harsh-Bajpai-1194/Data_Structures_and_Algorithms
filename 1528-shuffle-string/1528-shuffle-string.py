class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        L=[0]*len(s)
        for i in range(len(s)): L[indices[i]]=s[i]
        return "".join(L)