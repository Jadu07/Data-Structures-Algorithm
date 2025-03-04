class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                low = mid + 1
            else:
                high = mid - 1
        return high
