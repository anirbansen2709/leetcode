class Solution:
    def get_pow(self, x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        result = self.get_pow(x * x, n // 2)
        return result if n % 2 == 0 else result * x

    def myPow(self, x: float, n: int) -> float:
        result = self.get_pow(x, abs(n))
        return result if n > 0 else 1 / result

# TC - O(logn)
# SC - O(logn)
