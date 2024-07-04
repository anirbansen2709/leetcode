class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        while (n not in numbers) and (n != 1):
            numbers.add(n)
            temp = 0
            while n:
                last_digit = n % 10
                n = n // 10
                temp += (last_digit) ** 2
            n = temp
        return True if n == 1 else False

# TC - O(M * X)
# SC - O(M)
