import heapq
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        used_query = []
        available_query = []
        queries.sort(key=lambda x: x[0])
        query_pos = 0
        applied_count = 0
        for i in range(n):
            while query_pos < len(queries) and queries[query_pos][0] == i:
                end = queries[query_pos][1]
                heapq.heappush(available_query, -end)
                query_pos += 1
            nums[i] -= len(used_query)
            while nums[i] > 0 and available_query and -available_query[0] >= i:
                end = -heapq.heappop(available_query)
                heapq.heappush(used_query, end)
                nums[i] -= 1
                applied_count += 1
            if nums[i] > 0:
                return -1
            while used_query and used_query[0] == i:
                heapq.heappop(used_query)
        return len(queries)-applied_count