class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        L = [0] * 26
        for i in s:
            L[ord(i) - ord('a')] += 1
        for i in target:
            L[ord(i) - ord('a')] -= 1
        for i in range(len(target) - 1, -1, -1):
            cur = ord(target[i]) - ord('a')
            L[cur] += 1
            if any(x < 0 for x in L):
                continue
            nxt = -1
            for c in range(cur + 1, 26):
                if L[c]:
                    nxt = c
                    break
            if nxt == -1:
                continue
            L[nxt] -= 1
            ans = list(target[:i])
            ans.append(chr(nxt + ord('a')))
            for c in range(26):
                ans.extend(chr(c + ord('a')) * L[c])
            return ''.join(ans)
        return ""