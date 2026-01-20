class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        last = [0] * 32
        for i in range(n - 1, -1, -1):
            for b in range(32):
                if (nums[i] >> b) & 1:
                    last[b] = i
            max_last = i
            for b in range(32):
                max_last = max(max_last, last[b])
            answer[i] = max_last - i + 1
        return answer