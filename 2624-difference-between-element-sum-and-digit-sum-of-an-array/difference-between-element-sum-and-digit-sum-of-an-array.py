class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for i in nums:
            for character in str(i):
                digit_sum += int(character)

        return abs(element_sum - digit_sum)