class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L=nums1+nums2
        L.sort()
        n=len(L)
        if n%2==0:
            return float(L[n//2-1]+L[n//2])/2
        return L[n//2]