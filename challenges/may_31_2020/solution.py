class Solution:
    def lcs(self, A, B):
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        for i in range(len(A)+1):
            dp[i][0] = i
        for i in range(len(B)+1):
            dp[0][i] = i
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1]
                                   [j] + 1, dp[i][j - 1] + 1)
        # print(dp)
        return dp[len(A)][len(B)]

    def minDistance(self, word1: str, word2: str) -> int:
        return self.lcs(word1, word2)


s = Solution()
print(s.minDistance("horse", "ros"))
