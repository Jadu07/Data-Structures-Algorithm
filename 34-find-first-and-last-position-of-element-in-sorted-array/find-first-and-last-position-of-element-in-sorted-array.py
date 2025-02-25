class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        ans1 = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans1 = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        low = 0
        high = len(nums) - 1
        ans2 = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans2 = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [ans1, ans2]