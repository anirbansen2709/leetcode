# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the
# island's right and bottom edges. The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea 
# level of the cell at coordinate (r, c). The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's
# height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean. Return a 2D list of grid coordinates result where result[i] = 
# [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Logic
# Initialization: * It grabs the dimensions of the heights grid (self.rows and self.cols).It creates a 3D visited array (a 2D grid where
# every cell contains a list [0, 0]). The first index 0 tracks if a cell can reach the Pacific Ocean, and the second index 1 tracks if
# it can reach the Atlantic Ocean. Reverse Flow Traversal (DFS):Pacific: It loops through the top row and left column (the Pacific 
# border). For each cell, it triggers the traverse method, passing ocean=0.Atlantic: It loops through the bottom row and right column
# (the Atlantic border), triggering traverse with ocean=1.
# The traverse Helper Function:It marks the current cell as reachable for the specific ocean (changing 0 to 1).It checks the 4 
# neighboring cells.The Uphill Condition: If a neighbor is within bounds, hasn't been visited for this specific ocean yet, and its
# height is greater than or equal to ($\ge$) the current cell's height, it means water can flow down from that neighbor to the current 
# cell. So, it recursively calls traverse on that neighbor to continue the uphill path.
# Result Compilation: Finally, it iterates through the entire visited grid one last time. Any cell that has [1, 1] means it was 
# successfully reached by both the Pacific and Atlantic uphill traversals. It appends the coordinates (row, col) to the answer list.

class Solution:
    def is_valid(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return True
        return False 

    def traverse(self, row, col, ocean, visited):
        visited[row][col][ocean] = 1
        direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for del_row, del_col in direc:
            new_row = row + del_row
            new_col = col + del_col
            if self.is_valid(new_row, new_col) and visited[new_row][new_col][ocean] == 0 and self.heights[new_row][new_col] >= self.heights[row][col]:
                self.traverse(new_row, new_col, ocean, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.rows = len(heights)
        self.cols = len(heights[0])
        # pacific, atlantic
        visited = [[[0, 0] for _ in range(self.cols)] for _ in range(self.rows)]
        #atlantic
        for row in range(self.rows):
            self.traverse(row, 0, 0, visited)
            self.traverse(row, self.cols - 1, 1, visited)
        for col in range(self.cols):
            self.traverse(0, col, 0, visited)
            self.traverse(self.rows - 1, col, 1, visited)
        
        answer = []
        for row in range(self.rows):
            for col in range(self.cols):
                if visited[row][col] == [1, 1]:
                    answer.append((row, col))
        return answer
