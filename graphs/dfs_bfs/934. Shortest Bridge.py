from collections import deque

class Solution:
    def is_valid(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return True
        return False

    def dfs(self, row, col, visited):
        visited.add((row, col))
        direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for del_row, del_col in direc:
            new_row, new_col = row + del_row, col + del_col
            if self.is_valid(new_row, new_col) and (new_row, new_col) not in visited and self.grid[new_row][new_col] == 1:
                self.dfs(new_row, new_col, visited)
        return
    
    def bfs(self, visited):
        queue = deque(visited)
        steps = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for del_row, del_col in direc:
                    new_row, new_col = row + del_row, col + del_col
                    if self.is_valid(new_row, new_col) and (new_row, new_col) not in visited and self.grid[new_row][new_col] == 0:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                    if self.is_valid(new_row, new_col) and (new_row, new_col) not in visited and self.grid[new_row][new_col] == 1:
                        return steps
            steps += 1

    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    visited = set()
                    self.dfs(row, col, visited)
                    return self.bfs(visited)
