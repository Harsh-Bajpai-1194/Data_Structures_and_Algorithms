class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        L = []
        for i in nums:
            L1 = []
            while i > 0:
                L1.append(i % 10)
                i //= 10
            L.extend(L1[::-1])
        return L