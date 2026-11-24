class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = 9, 9
        def in_row(v, r, c):
            for col in range(cols):
                if col != c and board[r][col] == v:
                    return False
            return True
        
        def in_col(v, r, c):
            for row in range(rows):
                if row != r and board[row][c] == v:
                    return False
            return True
        
        def in_grid(v, r, c):
            row_group, col_group = r // 3, c // 3
            for row in range(row_group * 3, row_group * 3 + 3):
                for col in range(col_group * 3, col_group * 3 + 3):
                    if (row != r or col != c) and board[row][col] == v:
                        return False
            return True
        
        for r in range(rows):
            for c in range(cols):
                v = board[r][c]
                if v == '.':
                    continue
                if not in_row(v, r, c) or not in_col(v, r, c) or not in_grid(v, r, c):
                    return False
        
        return True