class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ans.append(nums[n])
        return ans
        