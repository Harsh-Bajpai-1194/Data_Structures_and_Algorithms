class Solution:
    def maxArea(self, height: List[int]) -> int:
        max=i=0
        j=len(height)-1
        while(i<j):
                a=min(height[i],height[j])*(j-i)
                if a>max: max=a
                if height[i]<height[j]: i=i+1
                else: j=j-1
        return max