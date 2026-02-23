class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        L=set()
        for i in range(len(s)-k+1):
            L.add(s[i:i+k])
            if len(L)==2**k: 
                return True
        return False