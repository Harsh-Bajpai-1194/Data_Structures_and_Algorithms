class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1=set(nums1)
        set2=set(nums2)
        L=[0,0]
        for i in nums1:
            if i in set2: L[0]+=1
        for i in nums2:
            if i in set1: L[1]+=1
        return L