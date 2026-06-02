class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        n = len(landStartTime)
        m = len(waterStartTime)
        minimum = float('inf')
        for i in range(n):
            for j in range(m):
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j]
                minimum = min(minimum, land_water)
                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i]
                minimum = min(minimum, water_land)
        return minimum