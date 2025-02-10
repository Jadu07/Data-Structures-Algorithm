class Solution:
    def addDigits(self, num: int) -> int:
        sum1 = 0 
        while(num>0):
            sum1 += num%10
            num = num//10
        num = sum1
        if(sum1>=10):
            return self.addDigits(num)
        else:
            return sum1

        