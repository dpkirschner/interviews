"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        
        result = []
        intervals.sort(key = lambda x: x[0] )
        current = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if current[1] >= interval[0]:
                if current[1] < interval[1]:
                    current[1] = interval[1]
            else:
                result.append(current)
                current = interval
        result.append(current)
        return result

if __name__ == "__main__":
    sol = Solution()
    
    assert sol.merge([[1,4],[4,5]]) == [[1,5]]
    assert sol.merge([[4,7],[1,4]]) == [[1,7]]
    assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    
    print("All test cases passed!")