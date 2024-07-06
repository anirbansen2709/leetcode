class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        intervals.sort()
        base = intervals[0]
        answer = []
        for idx in range(1, length):
            if base[1] < intervals[idx][0]:
                answer.append(base)
                base = intervals[idx]
            else:
                base[1] = max(base[1], intervals[idx][1])
        answer.append(base)
        return answer

#TC - O(nlogn)
#SC - O(1)
