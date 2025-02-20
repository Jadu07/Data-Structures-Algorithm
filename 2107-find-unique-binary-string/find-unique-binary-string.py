class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        arr=[]
        for i in range(0, len(nums)):
            if nums[i][i]=='0':
                arr.append('1')
            else:
                arr.append('0')
        return "".join(arr)
        