class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1  
        self.nums2 = nums2  
        self.freq = {}  
        for num in nums2:  
            if num in self.freq:  
                self.freq[num] += 1  
            else:  
                self.freq[num] = 1
    
    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]  
        self.freq[old_val] -= 1  
        if self.freq[old_val] == 0:  
            del self.freq[old_val]  
        self.nums2[index] += val  
        new_val = self.nums2[index]  
        if new_val in self.freq:  
            self.freq[new_val] += 1  
        else:  
            self.freq[new_val] = 1

    def count(self, tot: int) -> int:
        res = 0  
        for num in self.nums1:  
            complement = tot - num  
            if complement in self.freq:  
                res += self.freq[complement]  
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)