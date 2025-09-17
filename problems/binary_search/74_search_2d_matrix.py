"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # naive: binary search down rows
        # naive: binary search down columns
        left = 0
        right = len(matrix) - 1
        row = -1
        while left <= right:
            mid = left + ((right - left) // 2)
            if matrix[mid][0] > target:
                if mid == 0:
                    return False # can't go lower
                right = mid - 1
            elif matrix[mid][0] < target:
                if mid + 1 >= len(matrix) or matrix[mid + 1][0] > target:
                    row = mid # in this row
                    break
                left = mid + 1
            else:
                return True # we found it
            
        if row == -1:
            return False # safety
            
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if matrix[row][mid] > target:
                if mid == 0:
                    return False # can't go lower
                right = mid - 1
            elif matrix[row][mid] < target:
                if mid + 1 >= len(matrix[row]) or matrix[row][mid + 1] > target:
                    row = mid # in this row
                    break
                left = mid + 1
            else:
                return True # we found it
        return False
            
        

def test_solution():
    solution = Solution()

    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    result1 = solution.searchMatrix(matrix1, target1)
    expected1 = True
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: matrix = {matrix1}, target = {target1}")
    print(f"Output: {result1}")
    print()

    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    result2 = solution.searchMatrix(matrix2, target2)
    expected2 = False
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: matrix = {matrix2}, target = {target2}")
    print(f"Output: {result2}")

if __name__ == "__main__":
    test_solution()