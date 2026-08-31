class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = " ".join(map(str, nums))
        s = s.split()
        counts = {}
        L = []
        for i in s:
            counts[i] = counts.get(i, 0) + 1
            if counts[i] <= 2:
                L.append(int(i))
        for i in range(len(L)):
            nums[i] = L[i]
        return len(L)