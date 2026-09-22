class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        L=[]
        Output=[]
        i=1
        while (L!=target and i<=n):
            L.append(i)
            Output.append("Push")
            if L[-1]!=target[len(L)-1]:
                L.pop(-1)
                Output.append("Pop")
            i+=1
        return Output