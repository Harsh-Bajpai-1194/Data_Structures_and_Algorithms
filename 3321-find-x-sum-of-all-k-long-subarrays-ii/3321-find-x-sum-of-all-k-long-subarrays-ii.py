import heapq
from collections import defaultdict

class Solution(object):
    def findXSum(self, nums, k, x):
        res = []

        counts = defaultdict(int)
        for i in range(k):
            counts[nums[i]] += 1

        low = []

        for n, c in counts.items():
            heapq.heappush(low, (-c, -n))

        value = 0
        high = []
        high_nums = set()

        while len(high_nums) < x and low:
            c, n = heapq.heappop(low)
            heapq.heappush(high, (-c, -n))
            high_nums.add(-n)
            value += c * n

        res.append(value)

        def process_num(num):
            if num in high_nums:
                heapq.heappush(high, (counts[num], num))
            else:
                heapq.heappush(low, (-counts[num], -num))

        def clean_low():
            while low and (counts[-low[0][1]] != -low[0][0] or -low[0][1] in high_nums):
                heapq.heappop(low)

        def clean_high():
            while high and (counts[high[0][1]] != high[0][0] or high[0][1] not in high_nums):
                heapq.heappop(high)

        
        for i in range(k, len(nums)):
            leaving = nums[i - k]
            entering = nums[i]

            if leaving == entering:
                res.append(value)
                continue

            counts[leaving] -= 1
            counts[entering] += 1

            if leaving in high_nums:
                value -= leaving

            if entering in high_nums:
                value += entering

            process_num(leaving)
            process_num(entering)

            clean_low()
            clean_high()

            if low and high:
                if -low[0][0] > high[0][0] or (-low[0][0] >= high[0][0] and -low[0][1] > high[0][1]):
                    new_count, new_high = heapq.heappop(low)
                    old_count, old_high = heapq.heappop(high)
                    high_nums.remove(old_high)
                    high_nums.add(-new_high)

                    value -= (old_high * counts[old_high])
                    value += (-new_high * counts[-new_high])
                    heapq.heappush(high, (-new_count, -new_high))
                    heapq.heappush(low, (-old_count, -old_high))

            clean_low()

            if low and len(high_nums) < x:
                new_count, new_high = heapq.heappop(low)
                value += (-new_high * counts[-new_high])
                heapq.heappush(high, (-new_count, -new_high))
                high_nums.add(-new_high)

            res.append(value)

        return res