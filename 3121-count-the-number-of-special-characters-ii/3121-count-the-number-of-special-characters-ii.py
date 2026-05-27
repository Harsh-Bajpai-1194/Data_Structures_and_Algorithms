class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower,upper ={},{}
        for i, j in enumerate(word):
            if j.islower(): lower[j] = i
            elif j.isupper() and j not in upper: upper[j] = i
        c = 0
        for j in lower:
            upper_j = j.upper()
            if upper_j in upper and lower[j] < upper[upper_j]: c += 1
        return c