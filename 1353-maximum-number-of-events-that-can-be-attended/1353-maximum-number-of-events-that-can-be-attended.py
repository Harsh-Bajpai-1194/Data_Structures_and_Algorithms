class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        import heapq
        events.sort()  
        heap = []  
        day = 0  
        event_idx = 0  
        count = 0
        while heap or event_idx < len(events):  
            if not heap:  
                day = events[event_idx][0]
            while event_idx < len(events) and events[event_idx][0] <= day:  
                heapq.heappush(heap, events[event_idx][1])  
                event_idx += 1
            heapq.heappop(heap)  
            count += 1  
            day += 1
            while heap and heap[0] < day:  
                heapq.heappop(heap)
        return count