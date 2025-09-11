"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] in [0, 'Y']:
                    matrix[row][column] = 'X'
                    self.fill(matrix, row, column)
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 'X':
                    matrix[row][column] = 0
    
    def fill(self, matrix, row, column):
        for i in range(len(matrix[0])):
            if matrix[row][i] == 0 or matrix[row][i] == 'Y':
                matrix[row][i] = 'Y'
            else:
                matrix[row][i] = 'X'
        for i in range(len(matrix)):
            if matrix[i][column] == 0 or matrix[i][column] == 'Y':
                matrix[i][column] = 'Y'
            else:
                matrix[i][column] = 'X'
        
if __name__ == "__main__":
    solution = Solution()
    
    # matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    # solution.setZeroes(matrix1)
    # expected1 = [[1,0,1],[0,0,0],[1,0,1]]
    # print("Test 1:", "PASS" if matrix1 == expected1 else "FAIL")
    
    # matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # solution.setZeroes(matrix2)
    # expected2 = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    # print("Test 2:", "PASS" if matrix2 == expected2 else "FAIL")
    
    matrix3 = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    solution.setZeroes(matrix3)
    expected3 = [[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]]
    print("Test 3:", "PASS" if matrix3 == expected3 else "FAIL")