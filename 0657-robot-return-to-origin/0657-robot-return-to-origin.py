class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("R")==moves.count("L") and moves.count("U")==moves.count("D"):
            return True
        return False