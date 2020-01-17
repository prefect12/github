'''
56. Merge Intervals
Medium


Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        first, second = 0, 1
        intervals = sorted(intervals, key=lambda interval: interval[0])
        while second < len(intervals):

            if intervals[first][1] >= intervals[second][0] and intervals[first][1] <= intervals[second][1]:
                intervals.insert(first, [intervals[first][0], intervals[second][1]])
                intervals.pop(second)
                intervals.pop(second)

            elif intervals[first][1] >= intervals[second][0] and intervals[first][1] > intervals[second][1]:
                intervals.pop(second)

            else:
                first += 1
                second += 1

        return intervals
