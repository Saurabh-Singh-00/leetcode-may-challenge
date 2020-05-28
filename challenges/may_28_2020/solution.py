from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0, 1, 1, 2, 1, 2, 2, 3]
        if num < 8:
            return res[:num+1]
        for i in range(8, num+1):
            res.append(res[i % 8] + res[i//8])
        return res


s = Solution()
print(s.countBits(24))
