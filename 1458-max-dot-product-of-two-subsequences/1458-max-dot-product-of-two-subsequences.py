class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1),len(nums2)
        dp=[]
        for i in range(n + 1):
            dp.append([float('-inf')]*(m+1))
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                curr_product = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(curr_product,dp[i-1][j-1] + curr_product,dp[i-1][j],dp[i][j-1])
        return dp[n][m]