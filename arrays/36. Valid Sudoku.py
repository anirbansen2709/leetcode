from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = defaultdict(list)
        cols_dict = defaultdict(list)
        squares_dict = defaultdict(list)

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] != ".":
                    if (board[row][col] in rows_dict[row]) or (board[row][col] in cols_dict[col]) or (board[row][col] in squares_dict[(row // 3, col // 3)]):
                        return False
                    else:
                        rows_dict[row].append(board[row][col])
                        cols_dict[col].append(board[row][col])
                        squares_dict[(row // 3, col // 3)].append(board[row][col])
        
        return True


# TC - O(n * m)
# SC - O(n * m)
