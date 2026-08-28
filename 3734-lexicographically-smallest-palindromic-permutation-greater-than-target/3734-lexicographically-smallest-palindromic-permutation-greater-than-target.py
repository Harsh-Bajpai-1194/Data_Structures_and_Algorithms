class Solution:
    def isPossible(self, freq, cur, mid, target):
        f = freq[:]
        for i in range(25, -1, -1): cur += chr(97 + i) * f[i]
        cur += (mid if mid != '#' else '') + cur[::-1]
        return cur if cur > target else ""
    def lexPalindromicPermutation(self, s, target):
        if len(s) == 1: return s if s > target else ""
        freq = [s.count(chr(97 + i)) for i in range(26)]
        mid, oddCount = '#', 0
        for i in range(26):
            if freq[i] % 2:
                mid, oddCount = chr(97 + i), oddCount + 1
                freq[i] -= 1
            freq[i] //= 2
            if oddCount > 1: return ""
        res, prefix = "", ""
        for i in range(len(s) // 2):
            isThereAny = False
            for j in range(26):
                if freq[j]:
                    freq[j] -= 1
                    isPos = self.isPossible(freq, prefix + chr(97 + j), mid, target)
                    if isPos:
                        prefix += chr(97 + j)
                        isThereAny = True
                        res = min(res, isPos) if res else isPos
                        break
                    freq[j] += 1
            if not isThereAny: return ""
        return res