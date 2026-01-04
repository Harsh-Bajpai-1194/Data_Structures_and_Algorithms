class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict
        transitions = defaultdict(list)
        for p in allowed: transitions[(p[0], p[1])].append(p[2])
        memo = {}
        def solve(row):
            if len(row) == 1: return True
            if row in memo: return memo[row]
            def build(i, nxt):
                if i==len(row)-1: return solve(nxt)
                key = (row[i], row[i+1])
                if key not in transitions: return False
                for top in transitions[key]:
                    if build(i + 1, nxt + top):
                        return True
                return False
            res = build(0, "")
            memo[row] = res
            return res
        return solve(bottom)