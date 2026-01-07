class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()  
        n = len(events)  
        dp = {}
        def find_next_event(events, end_day):  
            left, right = 0, n  
            while left < right:  
                mid = (left + right) // 2  
                if events[mid][0] <= end_day:  
                    left = mid + 1  
                else:  
                    right = mid  
            return left
        def find_max_value(curr_index, count):  
            if count == 0 or curr_index == n:  
                return 0  
            if (curr_index, count) in dp:  
                return dp[(curr_index, count)]
            skip_event = find_max_value(curr_index + 1, count)  
            next_event_index = find_next_event(events, events[curr_index][1])  
            attend_event = events[curr_index][2] + find_max_value(next_event_index, count - 1)
            dp[(curr_index, count)] = max(skip_event, attend_event)  
            return dp[(curr_index, count)]
        return find_max_value(0, k)