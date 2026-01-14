from typing import List
import bisect
class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)
    def update(self, qleft, qright, qval, left, right, pos):
        if self.xs[right + 1] <= qleft or self.xs[left] >= qright: return
        if qleft <= self.xs[left] and self.xs[right + 1] <= qright: self.count[pos] += qval
        else:
            mid = (left + right) // 2
            self.update(qleft, qright, qval, left, mid, pos * 2 + 1)
            self.update(qleft, qright, qval, mid + 1, right, pos * 2 + 2)
        if self.count[pos] > 0: self.covered[pos] = self.xs[right + 1] - self.xs[left]
        else:
            if left == right: self.covered[pos] = 0
            else: self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]
    def query(self):
        return self.covered[0]
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs_set = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs_set.update([x, x + l])
        xs = sorted(xs_set)
        seg_tree = SegmentTree(xs)
        events.sort()
        psum = []
        widths = []
        y_coords = []
        total_area = 0.0
        prev_y = events[0][0]
        for y, delta, xl, xr in events:
            length = seg_tree.query()
            if y > prev_y:
                total_area += length * (y - prev_y)
                psum.append(total_area)
                y_coords.append(y)
                widths.append(length)
            seg_tree.update(xl, xr, delta, 0, seg_tree.n - 1, 0)
            prev_y = y
        target = total_area / 2.0
        idx = bisect.bisect_left(psum, target)
        if idx == 0:
            base_area = 0.0
            base_y = events[0][0]
        else:
            base_area = psum[idx - 1]
            base_y = y_coords[idx - 1]
        current_width = widths[idx]
        return base_y + (target - base_area) / current_width