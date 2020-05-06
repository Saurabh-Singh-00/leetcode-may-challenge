from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for i, a in enumerate(s):
            if d[a] == 1:
                return i
        return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
