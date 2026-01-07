class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        L=[0]*len(words)
        for i in range(len(words)):
            words[i]=list(set(words[i]))
            words[i].sort()
            words[i]="".join(words[i])
        for i in range(len(words)):
            for j in words[i]:
                if j in allowed: L[i]=1
                elif j not in allowed: 
                    L[i]=0
                    break
        return sum(L)