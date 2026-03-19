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
