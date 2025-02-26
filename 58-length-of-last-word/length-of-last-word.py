class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_word = s.split()
        last_word = split_word[-1]
        return(len(last_word))
        