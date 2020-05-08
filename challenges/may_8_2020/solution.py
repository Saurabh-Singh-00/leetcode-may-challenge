from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def slope(p1, p2):
            ans = 0
            try:
                ans = (p2[1] - p1[1]) / (p2[0] - p1[0])
            except ZeroDivisionError:
                ans = float('inf')
            return ans
        slope_start = slope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)-1):
            if not slope(coordinates[i], coordinates[i+1]) == slope_start:
                return False
        return True


s = Solution()
print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
