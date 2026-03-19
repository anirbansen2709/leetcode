# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Depth-First Search (DFS)
# Initialization: It sets up the dimensions of the grid (self.rows and self.cols), initializes a visited set to keep track of 
# coordinates that have already been explored, and sets the islands counter to 0.
# Grid Iteration: It uses nested loops to check every single cell in the grid. Triggering Traversal: If the loop encounters a cell
# containing "1" (land) that is not currently in the visited set, it means a new, unexplored island has been found. It increments the 
# islands count by 1 and calls the traverse helper method.
# DFS Traversal: The traverse method adds the current cell to the visited set. It then calculates the coordinates of the 4 adjacent
# neighbors (up, down, left, right) using the direc array. For any valid neighbor that is also a "1" and unvisited, it recursively 
# calls traverse to explore it. This effectively maps out the entire shape of that specific island and marks all its cells as visited
# so they aren't double-counted later.

class Solution:
    def is_valid(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return True
        return False

    def traverse(self, row, col, visited):
        visited.add((row, col))
        direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for del_row, del_col in direc:
            new_row = row + del_row
            new_col = col + del_col
            if self.is_valid(new_row, new_col) and self.grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                self.traverse(new_row, new_col, visited)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        visited = set()
        islands = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    self.traverse(row, col, visited)
        return islands

# TC - O(n * m)
# SC - O(n * m)
