class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        dp = [[-1] * 3 for i in range(len(events))]
        return self.find_events(events, 0, 0, dp)
    def find_events(self, events, idx, cnt, dp):
        if cnt == 2 or idx >= len(events): return 0
        if dp[idx][cnt] == -1:
            end = events[idx][1]
            lo, hi = idx + 1, len(events) - 1
            while lo < hi:
                mid = lo + ((hi - lo) >> 1)
                if events[mid][0] > end:
                    hi = mid
                else:
                    lo = mid + 1
            include = events[idx][2] + (self.find_events(events, lo, cnt + 1, dp)
            if lo < len(events) and events[lo][0] > end else 0)
            exclude = self.find_events(events, idx + 1, cnt, dp)
            dp[idx][cnt] = max(include, exclude)
        return dp[idx][cnt]