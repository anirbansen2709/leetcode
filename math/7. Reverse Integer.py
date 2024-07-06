import math

class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        max_int = (2 ** 31) - 1
        min_int = - (2 ** 31)
        while x:
            last_digit = int(math.fmod(x, 10))
            x = int(x/10)
            if (answer > max_int // 10) or (answer == max_int // 10 and last_digit > max_int % 10):
                return 0
            if (answer < min_int // 10) or (answer == min_int // 10 and last_digit < min_int % 10):
                return 0
            answer = answer * 10 + last_digit
        return answer

#TC - O(lenx)
#SC - O(1)
