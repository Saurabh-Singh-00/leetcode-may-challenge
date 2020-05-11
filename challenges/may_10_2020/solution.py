from typing import List
import collections


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            # When there is only one person and he trusts no one.
            return 1
        trusted_by = collections.defaultdict(set)
        trusts = collections.defaultdict(set)
        for t in trust:
            trusted_by[t[1]].add(t[0])
            trusts[t[0]].add(t[1])
        for b, a in trusted_by.items():
            if len(a) == N-1 and b not in a:
                if len(trusts[b]) == 0:
                    return b
        return -1


s = Solution()
print(s.findJudge(2, [[1, 2]]))
print(s.findJudge(3, [[1, 3], [2, 3]]))
print(s.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(s.findJudge(3, [[1, 2], [2, 3]]))
print(s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
