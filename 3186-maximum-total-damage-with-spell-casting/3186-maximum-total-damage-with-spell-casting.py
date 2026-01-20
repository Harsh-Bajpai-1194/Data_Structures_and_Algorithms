class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        count = collections.Counter(power)
        uniqueDamages = sorted(count.keys())
        dp = [[0] * 2 for _ in range(len(uniqueDamages))]
        for i, damage in enumerate(uniqueDamages):
            if i == 0:
                dp[0] = [0, damage * count[damage]]
                continue
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = damage * count[damage]
            if i >= 1 and uniqueDamages[i - 1] not in (damage - 1, damage - 2): dp[i][1]+=max(dp[i - 1])
            elif i >= 2 and uniqueDamages[i - 2] != damage - 2: dp[i][1] += max(dp[i - 2])
            elif i >= 3: dp[i][1] += max(dp[i - 3])
        return max(dp[-1])