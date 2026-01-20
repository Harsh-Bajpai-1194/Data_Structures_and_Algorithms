class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        n = len(stations)
        left = min(stations)
        right = sum(stations) + k + 1
        def check(stations, additionalStations, minPower):
            power = sum(stations[:r])
            for i in range(n):
                if i + r < n: power += stations[i + r]
                if power < minPower:
                    requiredPower = minPower - power
                    if requiredPower > additionalStations: return False
                    stations[min(n - 1, i + r)] += requiredPower
                    additionalStations -= requiredPower
                    power += requiredPower
                if i - r >= 0: power -= stations[i - r]
            return True
        while left < right:
            mid = (left + right) // 2
            if check(stations[:], k, mid): left = mid + 1
            else: right = mid
        return left - 1