class Solution:
    def minimumPushes(self, word):
        frequency = [0] * 26
        for c in word:
            frequency[ord(c) - ord("a")] += 1
        frequency.sort(reverse=True)
        total_pushes = 0  
        for i in range(26):
            if frequency[i] == 0:
                break
            total_pushes += (i // 8 + 1) * frequency[i]
        return total_pushes