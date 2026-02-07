class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return max(self._flip(s, k, 'NE'),self._flip(s, k, 'NW'),self._flip(s, k, 'SE'),self._flip(s, k, 'SW'))
    def _flip(self, s, k, direction):
        res = 0
        pos = 0
        opposite = 0
        for c in s:
            if c in direction:
                pos += 1
            else:
                pos -= 1
                opposite += 1
            res = max(res, pos + 2 * min(k, opposite))
        return res