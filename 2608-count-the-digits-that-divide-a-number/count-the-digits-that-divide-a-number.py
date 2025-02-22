class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        lst=list(str(num))
        for i in range(len(lst)):
            if num % int(lst[i]) == 0:
                count+=1
        return count