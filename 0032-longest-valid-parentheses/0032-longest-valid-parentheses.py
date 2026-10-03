class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        L = [-1]
        for i, c in enumerate(s):
            if c == '(': L.append(i)
            else:
                L.pop()
                if not L: L.append(i)
                else: res = max(res, i - L[-1])  
        return res