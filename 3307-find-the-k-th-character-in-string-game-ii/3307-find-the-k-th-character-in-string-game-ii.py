class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """ 
        operationsCount = int(math.ceil(math.log(k, 2)))
        increases = 0
        for i in range(operationsCount - 1, -1, -1):
            halfSize = 2 ** i
            if k > halfSize:
                k -= halfSize
                increases += operations[i]
        return string.ascii_lowercase[increases % 26]