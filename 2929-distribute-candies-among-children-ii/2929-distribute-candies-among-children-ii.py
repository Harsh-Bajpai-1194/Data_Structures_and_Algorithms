class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        def count_ways(total):
            if total < 0:
                return 0
            return (total + 2) * (total + 1) // 2
        total_ways = count_ways(n)
        over1 = count_ways(n - (limit + 1))
        over2 = count_ways(n - (limit + 1))
        over3 = count_ways(n - 2 * (limit + 1))
        return total_ways-3*over1+3*count_ways(n-2*(limit+1))-count_ways(n-3*(limit+1))