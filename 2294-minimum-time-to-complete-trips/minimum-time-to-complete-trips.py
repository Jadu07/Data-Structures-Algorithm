class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = max(time) * totalTrips

        while right > left:
            mid = (left + right)//2
            sums = sum([mid//t for t in time])
            if sums >= totalTrips:
                right = mid
            else:
                left = mid + 1
        
        return left   