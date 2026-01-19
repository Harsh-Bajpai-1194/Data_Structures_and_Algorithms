class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        trimmed = directions.lstrip('L').rstrip('R')
        return len(trimmed) - trimmed.count('S')