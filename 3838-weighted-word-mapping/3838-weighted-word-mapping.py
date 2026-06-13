class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        L=[]
        for i in words:
            s=0
            for j in i:
                s+=weights[ord(j)-ord("a")]
            L.append(chr(ord("z") - s % 26))
        return "".join(L)