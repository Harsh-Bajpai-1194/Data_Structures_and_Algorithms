class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        L=[0]*len(names)
        for i in range(len(L)):
            maximum=max(heights)
            index=heights.index(maximum)
            L[i]=names[index]
            heights[index]=0
        return L