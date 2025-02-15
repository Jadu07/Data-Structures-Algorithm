class Solution:
    def maxScore(self, s: str) -> int:
        count_1 = s[1:].count("1")
        max1 = float("-inf")
        count_0 = 0
        for i in range(len(s)-1):
            if(s[i] == "0"):
                count_0 += 1
            elif(i>0):
                count_1 -= 1
            max1 = max(count_0+count_1,max1)
        return max1
               