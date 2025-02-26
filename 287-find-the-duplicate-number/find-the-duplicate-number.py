class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_=set()
        for num in nums:
            if num in set_:
                return num
            else:
                set_.add(num)
        