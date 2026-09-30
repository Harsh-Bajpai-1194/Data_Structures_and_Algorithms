class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        L=[]
        depth=0
        n=len(seq)
        for i in range(n):
            if seq[i]=="(":
                L.append(depth % 2)
                depth=depth+1
            else:
                depth=depth-1
                L.append(depth % 2)
        return L