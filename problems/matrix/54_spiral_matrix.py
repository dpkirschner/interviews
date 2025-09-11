"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)

        count = right * bottom
        seen = 0

        result = []

        while len(result) < count:
            # Right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            if top >= bottom: break

            # Down
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            if right <= left: break

            # Left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            if bottom <= top: break

            # Up
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result
        

if __name__ == "__main__":
    solution = Solution()
    
    # matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    # result1 = solution.spiralOrder(matrix1)
    # expected1 = [1,2,3,6,9,8,7,4,5]
    # print("Test 1:", "PASS" if result1 == expected1 else "FAIL")
    
    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    result2 = solution.spiralOrder(matrix2)
    expected2 = [1,2,3,4,8,12,11,10,9,5,6,7]
    print("Test 1:", "PASS" if result2 == expected2 else "FAIL")