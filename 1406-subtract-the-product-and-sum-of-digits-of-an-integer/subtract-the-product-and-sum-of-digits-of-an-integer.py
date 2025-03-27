class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = list(str(n))
        
        prod = 1
        Sum = 0
        
        for i in arr:
            prod *= int(i)
            Sum += int(i)
        
        return prod - Sum