class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        memo = {}
        def dfs(pos1, pos2, total):
            if pos1 > pos2:
                pos1, pos2 = pos2, pos1
            key = (pos1, pos2, total)
            if key in memo:
                return memo[key]
            for i in range(1, total // 2 + 1):
                if (pos1 == i and pos2 == total - i + 1) or (pos2 == i and pos1 == total - i + 1):
                    return (1, 1)
            res_min, res_max = float('inf'), -float('inf')
            pairs = total // 2
            for mask in range(1 << pairs):
                win_pos = []
                l, r = 1, total
                for i in range(pairs):
                    if (mask >> i) & 1:
                        win_pos.append(l)
                    else:
                        win_pos.append(r)
                    l += 1
                    r -= 1
                if total % 2 == 1:
                    win_pos.append((total + 1) // 2)
                win_pos.sort()
                new_pos1 = new_pos2 = None
                for idx, p in enumerate(win_pos):
                    if p == pos1:
                        new_pos1 = idx + 1
                    if p == pos2:
                        new_pos2 = idx + 1
                if new_pos1 is None or new_pos2 is None:
                    continue
                nxt_min, nxt_max = dfs(new_pos1, new_pos2, len(win_pos))
                res_min = min(res_min, 1 + nxt_min)
                res_max = max(res_max, 1 + nxt_max)
            memo[key] = (res_min, res_max)
            return memo[key]
        res = dfs(firstPlayer, secondPlayer, n)
        return [res[0], res[1]]