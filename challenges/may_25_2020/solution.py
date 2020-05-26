from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        # Check for longest matching Subsequence [LCS लगा मुझे]
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # Actually I realized its LCS
        return dp[i][j]


s = Solution()
print(s.maxUncrossedLines(A=[2, 5, 1, 2, 5], B=[10, 5, 2, 1, 5, 2]))
print(s.maxUncrossedLines(A=[1, 3, 7, 1, 7, 5], B=[1, 9, 2, 5, 1]))
