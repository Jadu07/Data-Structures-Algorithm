class Solution:
    def isPowerOfFour(self, n: int) -> bool:    
        if n>0 and math.log(n,4).is_integer():
            return True
        else:
            return False