class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        L = []
        c = 0
        for i in s:
            if i == '(':
                if c > 0: L.append(i)
                c += 1
            else:
                c -= 1
                if c > 0: L.append(i)
        return "".join(L)