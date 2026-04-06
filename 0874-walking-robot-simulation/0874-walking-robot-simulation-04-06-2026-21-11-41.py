class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocked = set()
        for o in obstacles: blocked.add((o[0], o[1]))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, dir, maxDist = 0, 0, 0, 0
        for cmd in commands:
            if cmd == -1: dir = (dir + 1) % 4
            elif cmd == -2: dir = (dir + 3) % 4
            else:
                while cmd > 0:
                    nx = x + directions[dir][0]
                    ny = y + directions[dir][1]
                    if (nx, ny) in blocked: break
                    x, y = nx, ny
                    maxDist = max(maxDist, x * x + y * y)
                    cmd -= 1
        return maxDist