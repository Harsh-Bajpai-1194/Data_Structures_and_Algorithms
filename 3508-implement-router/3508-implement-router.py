class Router:
    from collections import deque, defaultdict
    from typing import List
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  
        self.seen = set()  
        self.dest_map = defaultdict(list)  

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.seen:
            return False  

        if len(self.queue) == self.memoryLimit:
            old = self.queue.popleft()
            self.seen.remove(old)
            d = old[1]
            if self.dest_map[d] and self.dest_map[d][0] == old[2]:
                self.dest_map[d].pop(0)

        self.queue.append(packet)
        self.seen.add(packet)
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.seen.remove(packet)
        d = packet[1]
        if self.dest_map[d] and self.dest_map[d][0] == packet[2]:
            self.dest_map[d].pop(0)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts_list = self.dest_map[destination]
        left, right = 0, len(ts_list)

        l, r = 0, len(ts_list)
        while l < r:
            mid = (l + r) // 2
            if ts_list[mid] < startTime:
                l = mid + 1
            else:
                r = mid
        left = l

        l, r = 0, len(ts_list)
        while l < r:
            mid = (l + r) // 2
            if ts_list[mid] <= endTime:
                l = mid + 1
            else:
                r = mid
        right = l
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)