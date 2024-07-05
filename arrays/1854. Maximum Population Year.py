class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = 2050 - 1950 + 1
        counts = [0 for _ in range(years)]
        for start, end in logs:
            counts[start - 1950] += 1
            counts[end - 1950] -= 1
        
        max_year = 1950
        max_pop = counts[0]
        for idx in range(1, years):
            counts[idx] += counts[idx - 1]
            if counts[idx] > max_pop:
                max_pop = counts[idx]
                max_year = 1950 + idx

        return max_year

# TC - O(max - years, n)
# SC - O(years/1)
