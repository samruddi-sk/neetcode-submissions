class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if any(board[r][col] == "Q" for r in range(row)):
                    continue
                if any(board[row-d][col-d] == "Q" for d in range(1, min(row, col)+1)):
                    continue
                if any(board[row-d][col+d] == "Q" for d in range(1, min(row, n-1-col)+1)):
                    continue

                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

        backtrack(0)
        return res