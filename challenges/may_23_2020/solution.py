from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            s, e = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
            if s <= e:
                res.append([s, e])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res


s = Solution()
print(s.intervalIntersection([[0, 2], [5, 10], [13, 23], [
      24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
