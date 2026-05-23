class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            L = []
            for j in range(i, n):
                L.append(nums[j])
            for j in range(i):
                L.append(nums[j])
            flag = True
            for j in range(n - 1):
                if L[j] > L[j + 1]:
                    flag = False
                    break
            if flag: return True
        return False