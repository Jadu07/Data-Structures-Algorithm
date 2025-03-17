class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for val in nums:
            subset += [ [val] + curr for curr in subset]
        
        return subset