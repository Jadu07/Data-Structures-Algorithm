class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        
        for i in range(len(nums)-2):
            base, side1, side2 = nums[i], nums[i+1], nums[i+2]
            if side1 + side2 > base:
                return base + side1 + side2

        return 0