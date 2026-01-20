class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        dp = [1] * n 
        prev = [-1] * n  
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if self.hamming_distance(words[i], words[j]) == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev[i] = j
        max_index = max(range(n), key=lambda x: dp[x])
        path = []
        while max_index != -1:
            path.append(words[max_index])
            max_index = prev[max_index]    
        return path[::-1]
    def hamming_distance(self, a, b):
        return sum(x != y for x, y in zip(a, b))
