import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        pattern, window = [0]*26, [0]*26
        def ctoi(x): return ord(x) - ord('a')
        for index in range(len(s1)):
            pattern[ctoi(s1[index])] += 1
            window[ctoi(s2[index])] += 1
        for i in range(len(s1), len(s2)):
            if pattern == window:
                return True
            window[ctoi(s2[i-len(s1)])] -= 1
            window[ctoi(s2[i])] += 1
        if pattern == window:
            return True
        return False


s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
print(s.checkInclusion("ab", "eidboaoo"))