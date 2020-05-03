class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ = [0]*26
        def to_int(x): return ord(x) - ord('a')
        for m in magazine:
            count_[to_int(m)] += 1
        for r in ransomNote:
            count_[to_int(r)] -= 1
            if count_[to_int(r)] < 0:
                return False
        return True


s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
