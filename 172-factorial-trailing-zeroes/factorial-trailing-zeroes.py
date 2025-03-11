class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n//5 + self.trailingZeroes(n//5) if n / 5 > 0 else 0

        