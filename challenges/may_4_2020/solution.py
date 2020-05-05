class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        return num ^ ((1 << num.bit_length()) - 1)

s = Solution()

print(s.findComplement(5))
print(s.findComplement(1))