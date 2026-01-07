class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        gain=[0]+gain
        for i in range(len(gain)-1): gain[i+1]+=gain[i]
        return max(gain)