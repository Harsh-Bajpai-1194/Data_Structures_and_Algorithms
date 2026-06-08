class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot: less.append(num)
            elif num > pivot: greater.append(num)
            else: equal.append(num)
        less.extend(equal)
        less.extend(greater)
        return less