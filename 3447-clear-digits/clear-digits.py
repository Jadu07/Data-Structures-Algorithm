class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for char in s:
            if '0' <= char <= '9':
                if ans:
                    ans.pop()
            else:
                ans.append(char)
        return ''.join(ans)