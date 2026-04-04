class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        R=rows
        if R == 1:
            return encodedText
        n = len(encodedText)
        C = n // R
        res = []
        for c in range(C):
            r, j = 0, c
            while r < R and j < C:
                res.append(encodedText[r * C + j])
                r += 1
                j += 1
        return "".join(res).rstrip()