import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or
                    board[r][c] in (box[(r//3,c//3)])):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                box[(r//3,c//3)].add(board[r][c])
        return True
            
example = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(example.isValidSudoku(board))
