class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        answer = []
        while top < bottom and left < right:
            for col in range(left, right):
                answer.append(matrix[top][col])
            top += 1
            for row in range(top, bottom):
                answer.append(matrix[row][right - 1])
            right -= 1
            if top >= bottom or left >= right:
                break
            for col in range(right - 1, left - 1, -1):
                answer.append(matrix[bottom - 1][col])
            bottom -= 1
            for row in range(bottom - 1, top - 1, - 1):
                answer.append(matrix[row][left])
            left += 1
        return answer

# TC - O(n * m)
# SC - O(1)
