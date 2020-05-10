class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num**(1/2)
        return (sqrt - int(sqrt)) < 0.0000001


s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
