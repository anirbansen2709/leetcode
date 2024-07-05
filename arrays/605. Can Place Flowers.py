class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        length = len(flowerbed)
        for idx in range(1, length - 1):
            if flowerbed[idx - 1] == flowerbed[idx] == flowerbed[idx + 1]:
                flowerbed[idx] = 1
                n -= 1
        return n < 1

# TC - O(n)
# SC - O(1)
