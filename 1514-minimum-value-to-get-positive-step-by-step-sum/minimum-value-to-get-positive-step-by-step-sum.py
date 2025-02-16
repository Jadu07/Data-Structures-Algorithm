class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre = []
        sum1 = 0
        for i in nums:
            sum1 += i
            pre.append(sum1)
        minn = min(pre)
        if(minn < 0):
            return 1-minn
        else:
            return 1