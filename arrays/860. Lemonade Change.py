class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_dict = {
            5 : 0,
            10 : 0,
            20 : 0
        }
        for bill in bills:
            bill_dict[bill] += 1
            remaining = bill - 5
            while remaining >= 10 and bill_dict[10] > 0:
                remaining -= 10
                bill_dict[10] -= 1
            while remaining >= 5 and bill_dict[5] > 0:
                remaining -= 5
                bill_dict[5] -= 1
            if remaining != 0:
                return False
        return True

# TC - O(n)
# SC - O(1)
