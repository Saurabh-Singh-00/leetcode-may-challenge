from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            if low == high:
                return nums[low]
            mid = low + (high - low)//2
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    low = mid + 2
                else:
                    high = mid
            else:
                if nums[mid] == nums[mid-1]:
                    low = mid + 1
                else:
                    high = mid - 1


s = Solution()
print(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
