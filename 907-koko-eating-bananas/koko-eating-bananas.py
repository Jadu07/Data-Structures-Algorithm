class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # R, L = max(piles), 1 
        # while L < R:
        #     mid = (R + L) // 2
        #     if sum(math.ceil(pile / mid) for pile in piles) <= h:
        #         R = mid
        #     else:
        #         L = mid + 1
                
        # return L


        def canFinish(speed):
            hours=0
            for pile in piles:
                hours+=(pile+speed-1)//speed
            return hours<=h
        
        left=1
        right=max(piles)
        result=right
        while left<=right:
            mid=(left+right)//2
            if canFinish(mid):
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result



        