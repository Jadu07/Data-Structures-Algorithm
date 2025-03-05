class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)

        def helper(mid):
            day = 1
            curr = 0
            for weight in weights:
                curr+=weight
                if curr>mid:
                    day+=1
                    curr = weight
            return day<=days

        while l<r:
            mid = (l+r)//2
            if helper(mid):
                r=mid
            else:
                l=mid+1
        return l