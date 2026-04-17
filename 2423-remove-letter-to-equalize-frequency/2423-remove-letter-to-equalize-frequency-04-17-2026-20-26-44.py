class Solution:
    def equalFrequency(self, word: str):
        L,L1=[],[]
        for i in word:
            if [i,word.count(i)] not in L:
                L.append([i,word.count(i)])
        for i in L:
            L1.append(i[1])
        L1.sort()
        if len(L1)==1 or len(set(L1))==1 and L1[0]==1:
            return True
        if len(L1)==2:
            return L1[0]==1 or L1[1]-L1[0]==1
        if L1[0]==1 and len(set(L1[1:]))==1:
            return True
        if L1[-1]-L1[-2]==1 and len(set(L1[:-1]))==1:
            return True
        return False