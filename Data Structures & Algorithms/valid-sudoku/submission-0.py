class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = [set() for i in range(len(board))]
        cols_set = [set() for i in range(len(board[0]))]
        box_set = [set() for i in range(len(board[0]))]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue

                box_idx = 3 * (r // 3) + (c // 3)

                if board[r][c] in rows_set[r] or board[r][c] in cols_set[c] or board[r][c] in box_set[box_idx]:
                    return False

                rows_set[r].add(board[r][c])
                cols_set[c].add(board[r][c])
                box_set[box_idx].add(board[r][c])

        return True