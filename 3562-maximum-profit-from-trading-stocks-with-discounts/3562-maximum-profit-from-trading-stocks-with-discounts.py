class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in hierarchy: 
            adj[u - 1].append(v - 1)
            
        def merge_knapsacks(dp1, dp2):
            new_dp = [-1] * (budget + 1)
            valid_costs_1 = [c for c, p in enumerate(dp1) if p != -1]
            valid_costs_2 = [c for c, p in enumerate(dp2) if p != -1]
            
            for c1 in valid_costs_1:
                for c2 in valid_costs_2:
                    if c1 + c2 <= budget:
                        new_profit = dp1[c1] + dp2[c2]
                        if new_profit > new_dp[c1 + c2]:
                            new_dp[c1 + c2] = new_profit
            return new_dp

        def dfs(u):
            children_if_u_buys = [-1] * (budget + 1)
            children_if_u_buys[0] = 0
            
            children_if_u_skips = [-1] * (budget + 1)
            children_if_u_skips[0] = 0
            
            for v in adj[u]:
                v_res_parent_bought, v_res_parent_skipped = dfs(v)
                children_if_u_buys = merge_knapsacks(children_if_u_buys, v_res_parent_bought)
                children_if_u_skips = merge_knapsacks(children_if_u_skips, v_res_parent_skipped)
            
            res_parent_bought = [-1] * (budget + 1)
            
            cost_discount = present[u] // 2
            profit_discount = future[u] - cost_discount
            if cost_discount <= budget:
                for c in range(budget - cost_discount + 1):
                    if children_if_u_buys[c] != -1:
                        total_cost = c + cost_discount
                        total_profit = children_if_u_buys[c] + profit_discount
                        if total_profit > res_parent_bought[total_cost]:
                            res_parent_bought[total_cost] = total_profit
            
            for c in range(budget + 1):
                if children_if_u_skips[c] != -1:
                    if children_if_u_skips[c] > res_parent_bought[c]:
                        res_parent_bought[c] = children_if_u_skips[c]

            res_parent_skipped = [-1] * (budget + 1)
            
            cost_full = present[u]
            profit_full = future[u] - cost_full
            if cost_full <= budget:
                for c in range(budget - cost_full + 1):
                    if children_if_u_buys[c] != -1: 
                        total_cost = c + cost_full
                        total_profit = children_if_u_buys[c] + profit_full
                        if total_profit > res_parent_skipped[total_cost]:
                            res_parent_skipped[total_cost] = total_profit
            
            for c in range(budget + 1):
                if children_if_u_skips[c] != -1:
                    if children_if_u_skips[c] > res_parent_skipped[c]:
                        res_parent_skipped[c] = children_if_u_skips[c]
            
            return res_parent_bought, res_parent_skipped
            
        i, root_res = dfs(0)
        return max(root_res)