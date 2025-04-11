class Solution(object):
    def removeOuterParentheses(self, s):
        ans = ''
        cnt = 0
        for ch in s:
            if ch == '(':
                if cnt:
                    ans += ch
                cnt += 1
            else:
                cnt -= 1
                if cnt:
                    ans += ch
        return ans