class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre=[0]*((len(gain))+1)
        for i in range(len(gain)):
            pre[i+1]=pre[i]+gain[i]
        return max(pre)