class Solution:
    def is_valid(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return True
        return False 

    def word_exist(self, row, col, idx, visited):
        if idx == len(self.word):
            return True
        if not self.is_valid(row, col) or self.board[row][col] != self.word[idx] or (row, col) in visited:
            return False
        visited.add((row, col))
        direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        result = False
        for del_row, del_col in direc:
            new_row = row + del_row
            new_col = col + del_col
            result = result or self.word_exist(new_row, new_col, idx + 1, visited)
        visited.remove((row, col))
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.word = word
        for row in range(self.rows):
            for col in range(self.cols):
                visited = set()
                if self.word_exist(row, col, 0, visited):
                    return True
        return False

#TC - O(n * m * k)
# SC - O(n * m)
