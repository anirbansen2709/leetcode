# Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent 
# cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# 
# 1. The Starting Point (exist method)The algorithm doesn't know where the word might start, so it iterates through every single cell in
# the m x n grid using a nested loop.For each cell, it initializes an empty visited set to keep track of the letters currently being used
# in the path.It kicks off the recursive DFS function word_exist starting at index 0 of the target word.If a path successfully finds the
# whole word, it immediately returns True. If it checks the entire board and finds nothing, it returns False.
# 2. The Core DFS & Backtracking (word_exist method) - This is where the actual searching happens. It checks the current cell and 
# explores its neighbors.
# Base Cases (When to stop): Success: If idx == len(self.word), it means all characters have been matched successfully, so it returns True.
# Failure: It returns False if: The coordinates are out of bounds (checked via is_valid). The character on the board doesn't match the
# current character we need (self.word[idx]). The cell has already been used in the current path (it is in the visited set).
# The Recursive Step (Exploring Neighbors): It marks the current valid cell as used by adding it to the visited set.
# It defines the four possible directions to move: right, left, down, and up (direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]).
# It loops through these directions, calculating the new_row and new_col, and recursively calls word_exist for the next letter (idx + 1).
# It uses result = result or ... meaning if any of the 4 directions successfully finds the rest of the word, result becomes True.
# Backtracking (The crucial step): After exploring all 4 directions from a specific cell, it executes visited.remove((row, col)).
# This "un-marks" the cell so that it can be used again by a completely different path that might start from somewhere else.


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

#TC - O(n * m * 4 ^ l) - n * m grid . L - length of word
# SC - O(n * m)
