class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)

        r = 0
        c = 0

        seen = set()

        for r in range(n):
            for c in range(n):

                num = board[r][c]

                if num == '.':
                    continue

                row = ("row", r, num)
                col = ("col", c, num)
                box_key = ("box", (r//3, c//3), num)

                if row in seen or col in seen or box_key in seen:
                    return False
                else:
                    seen.add(row) or seen.add(col) or seen.add(box_key)

        return True
