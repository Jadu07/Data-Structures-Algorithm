class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst=[]
        for i in range(len(accounts)):
            lst.append(sum(accounts[i]))
        return max(lst)

        