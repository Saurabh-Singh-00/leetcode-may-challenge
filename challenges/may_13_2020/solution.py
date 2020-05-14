class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        stack = []
        remove = k
        for digit in num:
            while remove and stack and stack[-1] > digit:
                stack.pop()
                remove -= 1
            stack.append(digit)
        res = "".join(stack[:len(num)-k]).lstrip("0")
        return res if len(res) else "0"


s = Solution()
print(s.removeKdigits("1432219", 3))
print(s.removeKdigits("10200", 1))
print(s.removeKdigits("10", 2))
