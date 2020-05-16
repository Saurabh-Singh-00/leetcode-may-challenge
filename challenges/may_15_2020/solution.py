from typing import List


class Solution:

    def kadane(self, A):
        # Kadane's Algo for Max continuous subarray sum
        n = len(A)
        global_max = 0
        local_max = 0
        for i in range(0, n):
            local_max = local_max + A[i]
            if (local_max < 0):
                local_max = local_max - A[i]
            if (global_max < local_max):
                global_max = local_max
        return global_max

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        max_kadane = self.kadane(A)
        max_invert = 0
        # Invert Signs
        for i in range(0, n):
            max_invert += A[i]
            A[i] = -A[i]

        max_invert = max_invert + self.kadane(A)
        if max_invert > max_kadane:
            return max_invert
        else:
            return max_kadane


s = Solution()
print(s.maxSubarraySumCircular([5, -3, 5]))
