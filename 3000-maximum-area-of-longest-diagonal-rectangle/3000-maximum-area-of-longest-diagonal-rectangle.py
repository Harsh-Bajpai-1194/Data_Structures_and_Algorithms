class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag = 0
        max_area = 0

        for l, w in dimensions:
            diag = math.sqrt(l * l + w * w)
            area = l * w

            if diag > max_diag or (abs(diag - max_diag) < 1e-9 and area > max_area):
                max_diag = diag
                max_area = area

        return max_area