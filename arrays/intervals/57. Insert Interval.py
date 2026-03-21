# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending 
# order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval. Insert newInterval into intervals such that intervals is
# still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary). Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Initialization: An empty list called answer is created to store the final merged intervals. Iteration: A for loop goes through each interval in the intervals array along with its index (idx).
# Condition 1: newInterval comes strictly BEFORE the current interval Code: if interval[0] > newInterval[1]: Logic: If the start time of the current interval is greater than the end time of 
# the newInterval, it means the newInterval fits perfectly right here without overlapping. Action: Because the rest of the array is already sorted and won't overlap with newInterval, the code
# simply appends newInterval to the answer, adds the remaining untouched intervals (intervals[idx:]), and returns the final result immediately.
# Condition 2: newInterval comes strictly AFTER the current interval Code: elif interval[1] < newInterval[0]: Logic: If the end time of the current interval is less than the start time of the 
# newInterval, there is no overlap and the current interval is fully processed. Action: The current interval is safely appended to the answer. The newInterval is carried forward to be compared
# against the next items in the loop.
# Condition 3: The intervals OVERLAP Code: else: Logic: If neither of the above is true, the intervals must overlap. Action: Instead of appending anything to the answer yet, the code merges
# them by updating the newInterval. It sets the start to the minimum of both start times, and the end to the maximum of both end times. This newly expanded newInterval is then carried into the
# next iteration to see if it overlaps with the next interval as well.
# Final Catch-All: Code: answer.append(newInterval) outside the loop. Logic: If the loop finishes without triggering Condition 1 (e.g., the newInterval belongs at the very end of the list, or 
# it merged with the last few items), the fully updated newInterval is appended to the answer right before returning it.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        for idx, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                answer.append(newInterval)
                return answer + intervals[idx:]
            elif interval[1] < newInterval[0]:
                answer.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1])
                ]
        answer.append(newInterval)
        return answer

# TC - O(n)
# SC - O(1)
