from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        sudoku rules
        1. no repeating in row
        2. no repeating in col
        3. no repeating in "box"

        3 no repeatings, i think imma use sets and a hashmap
        keys - row, col, (row//3, col//3)
        values - actual values in row/col/box

        Time: O(9^2) = O(1)
        Space: O(9^2) = O(1)
        """

        rows_map = defaultdict(set)
        cols_map = defaultdict(set)
        box_map = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows_map[r] or
                    board[r][c] in cols_map[c] or
                    board[r][c] in box_map[(r // 3, c // 3)]
                    ):
                    return False
                rows_map[r].add(board[r][c])
                cols_map[c].add(board[r][c])
                box_map[(r // 3, c // 3)].add(board[r][c])
        
        return True
