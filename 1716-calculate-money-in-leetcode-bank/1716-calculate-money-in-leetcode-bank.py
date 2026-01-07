class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 0
        monday_deposit = 1
        while n > 0:
            for day in range(7):
                if n == 0: break
                total_money += monday_deposit + day
                n -= 1
            monday_deposit += 1
        return total_money