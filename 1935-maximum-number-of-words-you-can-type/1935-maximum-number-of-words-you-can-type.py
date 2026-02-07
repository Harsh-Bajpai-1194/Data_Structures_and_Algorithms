class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split(" ")
        n=len(text)
        for i in text:
            for j in brokenLetters:
                if j in i:
                    n-=1
                    break
        return n