class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index,num in enumerate(nums):
            if(target-num in dic):
                return index,dic[target-num]
            else:
                dic[num] = index
        