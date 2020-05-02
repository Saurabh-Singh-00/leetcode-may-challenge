# sample first BAD version
BAD = 4


def isBadVersion(version):
    # Mock API isBadVersion(version)
    if version >= BAD:
        return True
    return False


class Solution:
    # Solution
    def binary_search_smallest(self, low, high):
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def firstBadVersion(self, n):
        return self.binary_search_smallest(1, n)


# Sample Test
s = Solution()
print(s.firstBadVersion(5))
