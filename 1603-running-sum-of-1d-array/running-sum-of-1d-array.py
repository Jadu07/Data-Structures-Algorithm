class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        pre[0]=nums[0]
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]+nums[i]
        return pre
