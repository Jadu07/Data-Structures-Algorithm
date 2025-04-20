class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res_right = 0
        curr = 0
        for num in nums:
            if num <= right:
                curr += 1
            else:
                curr = 0
            res_right += curr

        res_left = 0
        curr = 0
        for num in nums:
            if num < left:
                curr += 1
            else:
                curr = 0
            res_left += curr

        return res_right - res_left