class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        total_sum = 0
        for i in range(k):
            current_happiness = max(0, happiness[i] - i)
            if current_happiness == 0: break
            total_sum += current_happiness
        return total_sum