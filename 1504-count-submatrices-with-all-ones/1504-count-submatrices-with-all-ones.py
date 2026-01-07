class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1
            total += self.countSubmatInHistogram(heights)
        return total
    def countSubmatInHistogram(self, heights):
        n = len(heights)
        stack = []
        count = [0] * n
        ans = 0
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev = stack[-1]
                count[i] = count[prev] + heights[i] * (i - prev)
            else:
                count[i] = heights[i] * (i + 1)
            stack.append(i)
            ans += count[i]
        return ans