class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        pre = 0
        count = 0 
        for num in nums:
            pre += num
            remainder = pre%k
            if(remainder in dic):
                count += dic[remainder]
                dic[remainder] += 1
            else:
                dic[remainder] = 1
        return count
