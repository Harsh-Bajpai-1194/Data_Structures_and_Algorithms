class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        if len(items1)>len(items2):
            L=[i[0] for i in items1]
            for i in range(len(items2)):
                if items2[i][0] in L: items1[L.index(items2[i][0])][1]+=items2[i][1]
                else: items1.append(items2[i])
            items1.sort()
            return items1
        L=[i[0] for i in items2]
        for i in range(len(items1)):
            if items1[i][0] in L: items2[L.index(items1[i][0])][1]+=items1[i][1]
            else: items2.append(items1[i])
        items2.sort()
        return items2