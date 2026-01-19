class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        if not seats or len(seats) % 2 == 1: return 0
        res = 1
        mod = 10**9 + 7
        for i in range(2, len(seats), 2): res = (res * (seats[i] - seats[i-1])) % mod
        return res