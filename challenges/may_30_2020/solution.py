from typing import List


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:K]


s = Solution()
print(s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))
