class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minutes_angle = minutes * 6
        return min(abs(hour_angle - minutes_angle), 360-abs(hour_angle - minutes_angle))