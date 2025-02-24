from typing import List

class Solution:        
    def binary_search_on_row(self, matrix: List[List[int]], target: int, row: int) -> bool:
        m = len(matrix[0])
        left = 0
        right = m - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][m - 1]:
                return self.binary_search_on_row(matrix, target, mid)
            elif matrix[mid][m - 1] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
