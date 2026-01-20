class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]%(nums2[j]*k)==0: c+=1
        return c