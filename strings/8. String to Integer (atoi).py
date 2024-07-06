class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        answer = 0
        length = len(s)
        sign = +1
        int_max = (2 ** 31) - 1
        int_min = - (2 ** 31)
        while idx < length and s[idx] == " ":
            idx += 1
        if idx < length and s[idx] == "-":
            sign = -1
            idx += 1
        elif idx < length and s[idx] == "+":
            sign = +1
            idx += 1
        while idx < length and s[idx] in "0123456789":
            if (answer > int_max // 10) or (answer == int_max // 10 and int(s[idx]) > int_max % 10) : 
                return int_max if sign == +1 else int_min
            answer = answer * 10 + int(s[idx])
            idx += 1
        return answer * sign

# TC - O(n)
# SC - O(1)
