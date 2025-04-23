class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        no_delete = arr[0]  
        one_delete = 0      
        max_sum = arr[0]

        for i in range(1, n):
            one_delete = max(no_delete, one_delete + arr[i])
            no_delete = max(arr[i], no_delete + arr[i])
            max_sum = max(max_sum, no_delete, one_delete)

        return max_sum