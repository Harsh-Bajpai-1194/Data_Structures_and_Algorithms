class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        curr = set()
        for num in arr:
            curr = {num | x for x in curr} | {num}
            res |= curr
        return len(res)