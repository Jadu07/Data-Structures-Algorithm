class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lst1=[]
        lst2=[]
        for i in range(len(nums)):
            if nums[i]%2 == 0 :
                lst1.append(nums[i])
            else:
                lst2.append(nums[i])
        return lst1+lst2