class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        L=list(set(list(sentence)))
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i not in L:
                return False
        return True