class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        if (n==0): return 0
        Prefix_Max,Suffix_Max=[0]*n,[0]*n
        Prefix_Max[0]=height[0]
        for i in range(1,n): Prefix_Max[i]=max(Prefix_Max[i-1], height[i])
        Suffix_Max[n-1]=height[n-1]
        for i in range(n-2,-1,-1): Suffix_Max[i]=max(Suffix_Max[i+1], height[i])
        ans=0
        for i in range(n): ans+=min(Prefix_Max[i],Suffix_Max[i])-height[i]
        return ans