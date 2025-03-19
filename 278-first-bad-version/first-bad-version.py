# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        f = 1
        l = n
        found = -1
        while f<=l:
            mid = f + (l-f)//2
            if isBadVersion(mid):
                found = mid
                l = mid -1
            else:
                f = mid + 1
        return found