class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in s:
            if stack and i == stack[-1][0]:
                stack[-1][1] += 1
                
                if stack[-1][1] >= k:
                    stack.pop()
            else:
                stack.append([i, 1])
        
        res = ""
        for char, n in stack:
            res += char * n
        
        return res