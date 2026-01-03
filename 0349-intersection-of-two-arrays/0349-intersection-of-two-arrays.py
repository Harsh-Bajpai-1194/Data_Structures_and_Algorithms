class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L=[]
        for i in nums1:
            for j in nums2:
                if i not in L and i==j:
                    L.append(i)
        return L