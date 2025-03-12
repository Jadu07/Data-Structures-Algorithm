class Solution:
    def kthCharacter(self, k: int) -> str:
        cur = 'a'
        while len(cur) < k:
            new = ""
            for c in cur:
                if c == 'z':
                    new += 'a'
                else:
                    new += chr(ord(c)+1)
            cur += new
        return cur[k-1]

        