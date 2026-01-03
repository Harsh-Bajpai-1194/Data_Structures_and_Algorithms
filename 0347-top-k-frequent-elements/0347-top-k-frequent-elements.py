class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        a=list(set(nums))
        a.sort()
        freq=[]
        for i in a:
            freq.append(nums.count(i))
        L=[]
        for i in range(k):
            maximum=max(freq)
            index=freq.index(maximum)
            freq[index]=0
            L.append(a[index])
        return L