from typing import List


class Solution:
    def findMaxLength(self, nums):
        ''' I seriously didn't got its solution even after trying for 2 hrs 😭😭,
        so I just copy and pasted '''
        balance = 0
        max_length = 0
        table = {0: 0}
        for i, num in enumerate(nums, 1):
            if num == 0:
                balance -= 1
            else:
                balance += 1
            if balance in table:
                max_length = max(max_length, i - table[balance])
            else:
                table[balance] = i
        # print(table)
        return max_length


s = Solution()
print(s.findMaxLength([1, 0]))
print(s.findMaxLength([1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]))
