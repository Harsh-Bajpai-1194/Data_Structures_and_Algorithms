class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(set)
        for i,j in reservedSeats:
            if j in {4,5}: 
                seats[i].add(0) 
                seats[i].add(1)
            elif j in {6,7}: 
                seats[i].add(1)
                seats[i].add(2)
            elif j in {8,9}: seats[i].add(2)
            elif j in {2,3}: seats[i].add(0)
        res = 2*n
        for i in seats:
            if len(seats[i])==3: res -= 2
            else: res -= 1
        return res