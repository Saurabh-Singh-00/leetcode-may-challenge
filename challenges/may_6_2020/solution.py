import collections


class Solution:
    def majorityElement(self, nums) -> int:
        majority = len(nums) // 2
        frequency = collections.Counter(nums)
        for f in frequency.keys():
            if frequency[f] > majority:
                return f


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
