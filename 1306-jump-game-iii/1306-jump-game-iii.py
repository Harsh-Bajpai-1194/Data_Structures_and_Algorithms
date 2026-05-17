class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visited = set()
        while queue:
            curr = queue.pop(0) 
            if arr[curr] == 0: return True
            visited.add(curr)
            left_jump = curr - arr[curr]
            right_jump = curr + arr[curr]
            if left_jump >= 0 and left_jump not in visited: queue.append(left_jump)
            if right_jump < len(arr) and right_jump not in visited: queue.append(right_jump)
        return False