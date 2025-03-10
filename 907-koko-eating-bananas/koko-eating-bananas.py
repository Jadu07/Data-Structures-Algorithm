class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        R, L = max(piles), 1 
        while L < R:
            mid = (R + L) // 2
            if sum(math.ceil(pile / mid) for pile in piles) <= h:
                R = mid
            else:
                L = mid + 1
                
        return L

        