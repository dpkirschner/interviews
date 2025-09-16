"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
"""
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """


if __name__ == "__main__":
    solution = Solution()

    # Test 1
    input1 = 4
    expected1 = 2
    result1 = solution.totalNQueens(input1)
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: {input1}")
    print(f"Output: {result1}")

    # Test 2
    input2 = 1
    expected2 = 1
    result2 = solution.totalNQueens(input2)
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: {input2}")
    print(f"Output: {result2}")