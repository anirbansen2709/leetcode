class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []
        length = len(potions)
        for spell in spells:
            low = 0
            high = length - 1
            while low <= high:
                mid = ( low + high ) // 2
                if spell * potions[mid] >= success:
                    high = mid - 1
                else:
                    low = mid + 1
            answer.append(length - low)
        return answer
