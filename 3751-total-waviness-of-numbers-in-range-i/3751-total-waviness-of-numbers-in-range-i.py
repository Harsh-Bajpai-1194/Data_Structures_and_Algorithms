class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def waviness(n):
            s = str(n)
            return sum((a < b > c) or (a > b < c) for a, b, c in zip(s, s[1:], s[2:]))
        return sum(waviness(n) for n in range(num1, num2 + 1))