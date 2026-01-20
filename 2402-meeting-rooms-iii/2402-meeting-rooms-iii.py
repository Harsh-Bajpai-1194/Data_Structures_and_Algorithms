class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        rooms = [0] * n  
        available = list(range(n))  
        heap = []  
        meetings.sort()
        for start, end in meetings:  
            while heap and heap[0][0] <= start:  
                _, room = heapq.heappop(heap)  
                available.append(room)  
                available.sort()
            if available:  
                room = available.pop(0)  
                heapq.heappush(heap, (end, room))  
                rooms[room] += 1  
            else:  
                end_time, room = heapq.heappop(heap)  
                rooms[room] += 1  
                new_end = end_time + (end - start)  
                heapq.heappush(heap, (new_end, room))  
        max_meetings = max(rooms)  
        for i, count in enumerate(rooms):  
            if count == max_meetings:  
                return i