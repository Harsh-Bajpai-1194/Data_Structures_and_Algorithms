class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        before = [0, *accumulate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30])]  
        day = lambda mmdd: before[int(mmdd[:2]) - 1] + int(mmdd[3:])  
        return max(0, day(min(leaveAlice, leaveBob)) - day(max(arriveAlice, arriveBob)) + 1) 