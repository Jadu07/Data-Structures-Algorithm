class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        sum1 = 0

        for i in range(n):
            total_subarrays = (i + 1) * (n - i)
            odd_subarrays = (total_subarrays + 1) // 2  # Only counting odd-length ones
            sum1 += arr[i] * odd_subarrays

        return sum1
            