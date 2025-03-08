class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        mid = len(merged)//2

        if len(merged)%2==0:
            return (merged[mid-1]+merged[mid])/2
        return merged[mid]
