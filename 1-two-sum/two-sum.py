class Solution:
    def twoSum(self, nums, target):
        number_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in number_map:
             
                return [i, number_map[diff]]

           
            number_map[num] = i
        
        return None