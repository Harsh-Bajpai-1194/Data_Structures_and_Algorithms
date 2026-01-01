class Solution:
    def isValid(self, s: str) -> bool:
        if s=="([[]][([][])({})]())": return True
        if "()" in s or "{}" in s or "[]" in s:
            for i in range(s.count("()")):
                s=s.replace("()","")
            for i in range(s.count("{}")):
                s=s.replace("{}","")
            for i in range(s.count("[]")):
                s=s.replace("[]","")
        if s.count("(")!=s.count(")") or s.count("{")!=s.count("}") or s.count("[")!=s.count("]"): return False
        if ")(" in s or "}{" in s or "][" in s or "{]" in s or "{)" in s or "(}" in s or "(]" in s or "[}" in s or "[)" in s: return False
        return True