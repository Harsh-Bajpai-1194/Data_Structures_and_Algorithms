class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        A = nums
        groups = []
        gmap = {}
        for val in sorted(A):
            if not groups or val - groups[-1][-1] > limit:
                groups.append([])
            groups[-1].append(val)
            gmap[val] = len(groups) - 1
        itr = [iter(g) for g in groups]
        for i in range(len(A)):
            A[i] = next(itr[gmap[A[i]]])
        return A