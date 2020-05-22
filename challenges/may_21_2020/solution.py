from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    occur = min(dp[i][j], dp[i][j+1], dp[i+1][j])
                    dp[i+1][j+1] = occur + 1
                    count += dp[i+1][j+1]
        return count


s = Solution()
print(s.countSquares([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))
