class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        result, temp, j = 0, 0, 0
        for num in nums:
            while num in unique:
                unique.remove(nums[j])
                temp -= nums[j]
                j += 1
            unique.add(num)
            temp += num
            result = max(temp, result)
        return result