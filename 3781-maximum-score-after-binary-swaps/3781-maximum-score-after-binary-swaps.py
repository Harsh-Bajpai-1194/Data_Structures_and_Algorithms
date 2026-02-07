class Solution(object):
    def maximumScore(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        import heapq
        count,L=0,[]
        for i,j in enumerate(nums):
            heapq.heappush(L,j*(-1))
            if s[i]=="1" and L!=[]: count-=heapq.heappop(L)
        return count