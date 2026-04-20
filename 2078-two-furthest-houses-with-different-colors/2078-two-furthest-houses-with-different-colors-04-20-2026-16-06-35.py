class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maximum=0
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors)):
                if colors[j]!=colors[i]:
                    maximum=max(maximum,abs(j-i))
        return maximum