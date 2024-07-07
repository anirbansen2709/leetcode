class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 3, 4]
        #[1, 1, 1, 1]
        #[1, 1, 2, 6]
        #[24, 12, 8, 6]

        length = len(nums)
        answer = [1 for _ in range(length)]
        mult = 1

        for idx in range(1, length):
            answer[idx] = answer[idx - 1] *  nums[idx - 1]
        
        for idx in range(length - 2, - 1, -1):
            mult = mult * nums[idx + 1]
            answer[idx] = answer[idx] * mult
        
        return answer

# TC - O(n)
# SC - O(1)
