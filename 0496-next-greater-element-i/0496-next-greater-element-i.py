class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in range(len(nums1)):
            j=nums2.index(nums1[i])
            for k in range(j,len(nums2)):
                if nums2[k]>nums2[j]: 
                    L.append(nums2[k])
                    break
            else: L.append(-1)
        return L