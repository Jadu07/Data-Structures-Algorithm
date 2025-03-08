class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        srtd_arr=sorted(nums)
        differences=[]
        if len(nums) < 2:
            return 0
        for i in range(len(srtd_arr)-1):
            differences.append(srtd_arr[i+1]-srtd_arr[i])        
        return max(differences)