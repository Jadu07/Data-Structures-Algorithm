class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lst=""
        for ch in letters:
            if ch > target :
                lst=ch
                break
            if lst=="":
                lst=letters[0]
        return (lst)
