class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # If mid is a peak
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid

            # If mid is not a peak, check left or right
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                r = mid - 1  # Search left
            else:
                l = mid + 1  # Search right

        return l  # l and r will converge to a peak element

            
        