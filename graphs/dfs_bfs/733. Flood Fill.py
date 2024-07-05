class Solution:
    def is_valid(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols :
            return True
        return False

    def traverse(self, image, sr, sc, visited):
        image[sr][sc] = self.color
        visited.add((sr, sc))
        direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for del_row, del_col in direc:
            new_row = sr + del_row
            new_col = sc + del_col
            if self.is_valid(new_row, new_col) and (new_row, new_col) not in visited and image[new_row][new_col] == self.src_color:
                self.traverse(image, new_row, new_col, visited)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.src_color = image[sr][sc] 
        self.rows = len(image)
        self.cols = len(image[0])
        self.color = color
        visited = set()

        self.traverse(image, sr, sc, visited)

        return image

# TC - O(n * m)
# SC - O(n * m)
