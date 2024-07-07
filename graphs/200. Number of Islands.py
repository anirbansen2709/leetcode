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
