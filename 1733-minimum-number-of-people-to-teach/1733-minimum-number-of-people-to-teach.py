class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        from typing import List
        lang_sets = [set(l) for l in languages]
        need_fix = set()
        for u, v in friendships:
            if lang_sets[u-1].isdisjoint(lang_sets[v-1]):
                need_fix.add(u-1)
                need_fix.add(v-1)
        res = float('inf')
        for lang in range(1, n+1):
            count = 0
            for user in need_fix:
                if lang not in lang_sets[user]:
                    count += 1
            res = min(res, count)
        return 0 if res == float('inf') else res