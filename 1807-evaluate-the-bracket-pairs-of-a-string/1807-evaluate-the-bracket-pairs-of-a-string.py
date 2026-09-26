class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        L, index = [], -1
        for i, c in enumerate(s):
            if c == "(":
                index = i
            elif c == ")":
                L.append(d.get(s[index + 1 : i], "?"))
                index = -1
            elif index < 0:
                L.append(c)
        return "".join(L)