class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(len(arr) - len(arr)//4):
            if arr[i] == arr[i + len(arr)//4]:
                return arr[i]