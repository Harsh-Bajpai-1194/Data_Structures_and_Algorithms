class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s, first, second, val):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += val
                else:
                    stack.append(ch)
            return "".join(stack), score
        if x > y:
            s, score1 = remove_pattern(s, 'a', 'b', x)
            _, score2 = remove_pattern(s, 'b', 'a', y)
        else:
            s, score1 = remove_pattern(s, 'b', 'a', y)
            _, score2 = remove_pattern(s, 'a', 'b', x)
        return score1 + score2