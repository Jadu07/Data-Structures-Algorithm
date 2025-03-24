class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud, lr = 0, 0
        for char in moves:
            match char:
                case 'U':
                    ud += 1
                case 'D':
                    ud -= 1
                case 'L':
                    lr -= 1
                case 'R':
                    lr += 1
        return (ud, lr) == (0, 0)
        
        