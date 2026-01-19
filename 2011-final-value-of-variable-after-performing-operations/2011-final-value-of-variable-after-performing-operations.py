class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations: x=x+1 if '+' in i else x-1
        return x