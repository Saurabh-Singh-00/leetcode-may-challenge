import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        return ''.join(sorted(sorted(s), key=counter.get, reverse=True))


s = Solution()
print(s.frequencySort("tree"))
print(s.frequencySort("cccaaa"))
print(s.frequencySort("Aabb"))
