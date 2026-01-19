class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p,n=[],[]
        for i in nums:
            if i<0: n.append(i)
            else: p.append(i)
        L=[]
        for i in range(len(nums)):
            if i%2==0: L.append(p[i//2])
            else: L.append(n[i//2])
        return L