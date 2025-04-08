class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre=[0]*len(nums)
        pre[0]=nums[0]
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]+nums[i]
        # print(pre)

        for j in range(len(nums)):

            if pre[j]==pre[(len(nums)-1)]- (pre[j-1] if(j>0) else 0):
                res=j
                break
            else:
                res= -1
        return (res)