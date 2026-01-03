class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res,curr=[],1
        for i in range(n):
            res.append(curr)
            if curr*10<=n:
                curr*=10
            else:
                while curr%10==9 or curr+1>n:
                    curr//=10
                curr+=1
        return res