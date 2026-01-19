class Solution:
    def minimumSum(self, num: int) -> int:
        minimum=num
        num=str(num)
        L=[]
        for i in range(len(num)):
            for j in range(len(num)):
                if i!=j: L.append([num[i],num[j]])
        for i in range(len(L)): L[i]=str(L[i][0])+str(L[i][1])
        num=list(num)
        num.sort()
        num="".join(num)
        for i in range(len(L)-1):
            for j in range(i+1,len(L)):
                a=L[i]+L[j]
                a=list(a)
                a.sort()
                a="".join(a)
                if a==num:
                    if int(L[i])+int(L[j])<minimum: minimum=int(L[i])+int(L[j])
        return minimum