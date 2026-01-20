class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        diffs=[]
        total=0
        for num in nums:
            xor_val =num^k
            total+=num
            diffs.append(xor_val - num)
        diffs.sort(reverse=True)
        max_gain = 0
        for i in range(0, len(nums), 2): 
            if i + 1 >= len(nums): break
            gain_pair = diffs[i] + diffs[i + 1]
            if gain_pair > 0:
                max_gain += gain_pair
            else:
                break
        return total+max_gain