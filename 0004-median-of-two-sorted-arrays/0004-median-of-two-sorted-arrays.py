class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        L=nums1+nums2
        L.sort()
        n=len(L)
        if n%2==0:
            return float(L[n//2-1]+L[n//2])/2
        return L[n//2]