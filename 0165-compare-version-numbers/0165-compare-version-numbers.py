class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n = max(len(v1), len(v2))
        v1.extend([0] * (n - len(v1)))
        v2.extend([0] * (n - len(v2)))
        for i in range(n):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0