"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        results = []
        current_merge = newInterval
        for interval in intervals:
            if current_merge is not None and current_merge[1] < interval[0]:
                results.append(current_merge)
                current_merge = None
            if current_merge is None:
                results.append(interval)
            elif (current_merge[1] < interval[0] or current_merge[0] > interval[1]):
                # no overlap
                results.append(interval)
            else:
                current_merge = [min(interval[0], current_merge[0]), max(interval[1], current_merge[1])]

        if current_merge is not None:
            results.append(current_merge)
        return results

if __name__ == "__main__":
    sol = Solution()
    
    # assert sol.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    # assert sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    # assert sol.insert([], [5,7]) == [[5,7]]
    assert sol.insert([[1,5]], [2,3]) == [[1,5]]
    
    print("All test cases passed!")
