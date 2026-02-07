class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, index, l, r):
        if l == r:
            self.tree[index] = nums[l]
        else:
            mid = (l + r) // 2
            self.build(nums, 2 * index + 1, l, mid)
            self.build(nums, 2 * index + 2, mid + 1, r)
            self.tree[index] = max(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def update(self, idx, val):
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, index, l, r, idx, val):
        if l == r:
            self.tree[index] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self._update(2 * index + 1, l, mid, idx, val)
            else:
                self._update(2 * index + 2, mid + 1, r, idx, val)
            self.tree[index] = max(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def query_first(self, target):
        return self._query_first(0, 0, self.n - 1, target)

    def _query_first(self, index, l, r, target):
        if self.tree[index] < target:
            return -1
        if l == r:
            self.update(l, -1)
            return l
        mid = (l + r) // 2
        if self.tree[2 * index + 1] >= target:
            return self._query_first(2 * index + 1, l, mid, target)
        else:
            return self._query_first(2 * index + 2, mid + 1, r, target)
class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        tree = SegmentTree(baskets)
        unplaced = 0
        for fruit in fruits:
            if tree.query_first(fruit) == -1:
                unplaced += 1
        return unplaced