class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter()
        for fruit in basket1:
            count[fruit] += 1
        for fruit in basket2:
            count[fruit] -= 1

        to_swap = []
        for fruit, freq in count.items():
            if freq % 2 != 0:
                return -1
            to_swap.extend([fruit] * (abs(freq) // 2))

        to_swap.sort()
        min_val = min(min(basket1), min(basket2))
        n = len(to_swap) // 2
        total_cost = 0
        for i in range(n):
            total_cost += min(to_swap[i], 2 * min_val)

        return total_cost