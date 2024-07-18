from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda : defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x, y = point
        for y_val in self.points[x]:
            if y_val == y:
                continue
            delta = abs(y_val - y)
            count += (self.points[x][y_val] * self.points[x + delta][y_val] * self.points[x + delta][y])
            count += (self.points[x][y_val] * self.points[x - delta][y_val] * self.points[x - delta][y])
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
