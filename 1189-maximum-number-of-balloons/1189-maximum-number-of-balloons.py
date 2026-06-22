class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        string = Counter(text)
        return min(string["b"], string["a"], string["l"]>>1, string["o"]>>1, string["n"])