class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(set(arr))
        L={j:i+1 for i,j in enumerate(a)}
        return [L[i] for i in arr]