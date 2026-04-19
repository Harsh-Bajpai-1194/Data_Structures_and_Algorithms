class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i,j=0,1
        while i<len(nums1) and j<len(nums2):
            i+=nums1[i]>nums2[j]
            j+=1
        return j-i-1