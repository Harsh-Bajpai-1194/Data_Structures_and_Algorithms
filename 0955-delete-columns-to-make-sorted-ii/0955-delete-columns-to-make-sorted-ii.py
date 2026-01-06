class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])
        sorted_pairs = [False] * (n - 1)
        deletions = 0
        for j in range(m):
            conflict = False
            for i in range(n - 1):
                if not sorted_pairs[i]:
                    if strs[i][j] > strs[i+1][j]:
                        conflict = True
                        break
            if conflict: deletions += 1
            else:
                for i in range(n - 1):
                    if not sorted_pairs[i]:
                        if strs[i][j] < strs[i+1][j]:
                            sorted_pairs[i] = True    
        return deletions