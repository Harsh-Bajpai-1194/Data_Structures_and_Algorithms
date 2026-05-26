class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=""
        for i in set(word):
            s=s+(i if 65<=ord(i)<=90 and chr(ord(i)+32) in set(word) else "")
        return len(s)