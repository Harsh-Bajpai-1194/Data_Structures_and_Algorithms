class Solution:
    q = [*range(1, 10)]
    for i in q:
        d = i % 10
        if d < 9: q.append(i * 10 + d + 1)
    def sequentialDigits(self, low: int, high: int):
        return [i for i in self.q if low <= i <= high]