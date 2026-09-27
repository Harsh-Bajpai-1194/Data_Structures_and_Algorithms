class Solution:
    def reverseParentheses(self, s: str) -> str:
        L = deque()
        L1 = []
        for i in s:
            if i == "(": L.append(len(L1))
            elif i == ")":
                start = L.pop()
                L1[start:] = L1[start:][::-1]
            else: L1.append(i)
        return "".join(L1)