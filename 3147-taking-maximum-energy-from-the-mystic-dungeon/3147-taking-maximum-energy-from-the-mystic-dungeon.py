class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        L=energy
        for i in range(len(energy)-k-1,-1,-1): L[i]+=L[i+k]
        return max(L)