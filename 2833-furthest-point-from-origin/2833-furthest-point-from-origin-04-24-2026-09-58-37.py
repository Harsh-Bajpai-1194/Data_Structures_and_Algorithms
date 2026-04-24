class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a=moves.count("L")
        b=moves.count("R")
        c=b-a
        if c>=0: return c+moves.count("_")
        return -(c-moves.count("_"))