class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a)
        lenb = len(b)
        max_len = max(lena, lenb)
        a = "0" * (max_len - lena) + a
        b = "0" * (max_len - lenb) + b

        sum_binary = ""
        carry = 0
        for idx in range(max_len - 1, -1, -1):
            total = int(a[idx]) + int(b[idx]) + carry
            carry = total // 2
            total = total % 2
            sum_binary = str(total) + sum_binary
        
        return "1" + sum_binary if carry else sum_binary


# TC - O(maxlen a, b)
# SC - O(1)
