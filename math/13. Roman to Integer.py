class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }

        idx = 0
        total = 0
        length = len(s)

        while idx < length:
            if idx < length - 1 and s[idx : idx + 2] in symbol_dict:
                total += symbol_dict[s[idx : idx + 2]]
                idx += 2
            else:
                total += symbol_dict[s[idx : idx + 1]]
                idx += 1
        
        return total

# TC - O(n)
# SC - O(1)
