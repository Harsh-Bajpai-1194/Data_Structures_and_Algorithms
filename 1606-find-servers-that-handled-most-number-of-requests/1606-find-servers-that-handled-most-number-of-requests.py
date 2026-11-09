class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        active_tasks = []
        available = list(range(k))
        counts = [0] * k
        for req_idx, (arr_time, process_time) in enumerate(zip(arrival, load)):
            while active_tasks and active_tasks[0][0] <= arr_time:
                _, srv_idx = heappop(active_tasks)
                heappush(available, req_idx + (srv_idx - req_idx) % k)
            if available:
                srv_idx = heappop(available) % k
                counts[srv_idx] += 1
                heappush(active_tasks, (arr_time + process_time, srv_idx))
        max_reqs = max(counts)
        return [idx for idx, val in enumerate(counts) if val == max_reqs]