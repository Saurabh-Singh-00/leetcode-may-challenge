from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pattern, window, result = [0]*26, [0]*26, []
        def ctoi(x): return ord(x) - ord('a')
        for index in range(len(p)):
            pattern[ctoi(p[index])] += 1
            window[ctoi(s[index])] += 1
        for i in range(len(p), len(s)):
            if pattern == window:
                result.append(i-len(p))
            window[ctoi(s[i-len(p)])] -= 1
            window[ctoi(s[i])] += 1
        if pattern == window:
            result.append(len(s) - len(p))
        return result


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
