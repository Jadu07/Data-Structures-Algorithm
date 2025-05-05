class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = 0
        while colors[i] == colors[n - 1]:
            i += 1
        j = n - 1
        while colors[j] == colors[0]:
            j -= 1
        return max(n - 1 - i, j)