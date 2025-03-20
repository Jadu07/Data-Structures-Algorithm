class Solution:
    def arrangeCoins(self, n: int) -> int:
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            value=(mid*(mid+1))//2
            if value==n:
                return mid
            elif value<n:
                left=mid+1
            else:
                right=mid-1
        return right
        