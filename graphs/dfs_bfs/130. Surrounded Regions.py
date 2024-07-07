class Solution:
    def is_valid(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols :
            return True
        return False

    def traverse(self, row, col, visited):
        visited.add((row, col))
        direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for del_row, del_col in direc:
            new_row, new_col = row + del_row, col + del_col
            if self.is_valid(new_row, new_col) and self.board[new_row][new_col] == "O" and (new_row, new_col) not in visited:
                self.traverse(new_row, new_col, visited)
        return

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        visited = set()
        for row in range(self.rows):
            if self.board[row][0] == "O":
                self.traverse(row, 0, visited)
            if self.board[row][self.cols - 1] == "O":
                self.traverse(row, self.cols - 1, visited)
        for col in range(self.cols):
            if self.board[0][col] == "O":
                self.traverse(0, col, visited)
            if self.board[self.rows - 1][col] == "O":
                self.traverse(self.rows - 1, col, visited)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == "O" and (row, col) not in visited:
                    self.board[row][col] = "X"

# TC - O(n * m)
# SC - O(n * m)
