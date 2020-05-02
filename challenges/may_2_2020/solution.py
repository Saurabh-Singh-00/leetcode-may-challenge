class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = [0]*255
        jewel_count = 0
        for j in J:
            jewels[ord(j) - ord('A')] = 1
        for s in S:
            if jewels[ord(s) - ord('A')]:
                jewel_count += 1
        return jewel_count


s = Solution()
print(s.numJewelsInStones("z", "ZZ"))
